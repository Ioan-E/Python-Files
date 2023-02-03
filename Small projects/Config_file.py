from shutil import copy
import time
import os


class ConfigFile():
    def __init__(self, filename, sep='='):

        self.filename = filename
        self.sep = sep
        self.config = {}

    def set(self, name, value):
        self.config[name] = str(value)

    def get(self, name):
        return self.config[name]

    def dump(self):
        with open(self.filename, 'w') as outfile:
            for key, value in self.config.items():
                outfile.write(f'{key}{self.sep}{value}\n')

    def load(self):
        self.config = {}
        for one_line in open(self.filename):
            key, value = one_line.strip().split(self.sep, 1)
            self.config[key] = value
        print(self.config)

    def __eq__(self, other):
        return self.config == other.config

    def __lt__(self, other):
        return set(self.config) < set(other.config)

    def __gt__(self, other):
        return set(self.config) > set(other.config)

    def __format__(self, format_code):
        if not format_code or format_code == 'short':
            return f'Filename {self.filename}: {self.config}'
        elif format_code == 'long':
            output = f'{self.filename}\n'
            output += '\n'.join([f'{key}={value}'
                                 for key, value in self.config.items()])
            output += '\n'
            return output
        elif format_code == 'stats':
            return f'ConfigFile {self.filename}, with {len(self.config)} key-value pairs'
        else:
            raise TypeError(f'Unknown format code {format_code}')

    def __enter__(self):
        self.load()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.dump()

class ConfigFileWithBackups(ConfigFile):
    def timestamp_filename(self, timestamp):
        dirname, filename = os.path.split(self.filename)
        new_filename = f'{timestamp}-{filename}'
        return os.path.join(dirname, new_filename)

    def dump(self):
        super().dump()
        copy(self.filename,
             self.timestamp_filename(time.time()))

    def restore(self, timestamp):
        old_filename = self.filename
        self.filename = self.timestamp_filename(timestamp)
        super().load()
        self.filename = old_filename
        super().dump()


# my_config_file = ConfigFileWithBackups('mycofig.txt')
# my_config_file.set('a', '2')
# my_config_file.set('b', '3')
# my_config_file.dump()
# print(my_config_file.config)
# print(f'{my_config_file}')

# my_config_file.restore(1675078956.507426)
# print(my_config_file.get('b'))

# my_config_file2 = ConfigFileWithBackups('myconfig2.txt')
# my_config_file2.set('a', '3')
# print(my_config_file < my_config_file2)

# with ConfigFile('mycofig.txt') as cf:
#     cf.set('c', 'success')
    
