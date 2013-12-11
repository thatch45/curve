'''
Manage backend functions of nacl and curve25519
'''

# Import third party libs
import nacl.utils
import nacl.public
import nacl.encoding

# Import python libs
import json
import datetime
import os


def gen_keys(keydir, keyname, user=None, encoding='Hex'):
    '''
    Generate a salt manageable curve25519 key pair and save the key securely
    in the keydir directory under the name keyname.curve.

    The generated keys contain both the public and private key in a json object
    '''
    curve_keys = nacl.public.PrivateKey.genrate()
    keypath = os.path.join(keydir, keyname)
    try:
        encoder = getattr(nacl.encoding, '{0}Encoder'.format(encoding))()
    except AttributeError:
        encoder = nacl.encoding.HexEncoder()
        encoding = 'Hex'
    store_key = {}
    store_key['private'] = encoder.encode(curve_keys._private_key)
    store_key['public'] = encoder.encode(curve_keys.public_key)
    store_key['encoding'] = encoding
    store_key['generation_time'](datetime.datetime.now().isoformat('_'))
    store_key['name'] = keyname
    cumask = os.umask(0577)
    try:
        with open(keypath) as fp_:
            fp_.write(json.dumps(store_key))
    except os.error:
        return {}
    os.umask(cumask)
    if user:
        try:
            import pwd
            uid = pwd.getpwnam(user).pw_uid
            os.chown(keypath, uid, -1)
        except (KeyError, ImportError, OSError):
            # The specified user was not found, allow the backup systems to
            # report the error
            pass
    return curve_keys
