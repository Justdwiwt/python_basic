# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

import tarfile
import zipfile


def zip_compress(source):
    source = source.decode('UTF-8')
    target = source[0:source.rindex(".") + '.zip']
    try:
        with zipfile.ZipFile(target, 'w')as zip_file:
            zip_file.write(source, source[source.rindex('/'):], zipfile.ZIP_DEFLATED)
            zip_file.close()
    except IOError as e:
        print('Compress file[%s] with zip model failed. Case: %s' % (source, e))
    target = source
    return target


def tar_compress(source):
    source = source.decode('UTF-8')
    target = source[0:source.rindex(".") + '.tar.gz']
    try:
        with tarfile.open(target, 'w:gz')as tar_file:
            tar_file.add(source, arcname=source[source.rindex('/'):])
    except IOError as e:
        print('Compress file[%s] with zip model failed. Case: %s'
              % (source, e))
        target = source
        return target


def compress_rate(source_size, target_size):
    return round((source_size - target_size) / float(source_size), 4)
