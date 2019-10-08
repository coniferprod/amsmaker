import math

waveform_params = {
    'saw': { 'a': 1.0, 'b': 0.0, 'c': 0.0, 'xp': 0.0, 'd': 0.0, 'e': 0.0, 'yp': 0.0 },
    'pluckedString': { 'a': 2.0, 'b': 1.0, 'c': 0.0, 'xp': 0.2, 'd': 0.0, 'e': 0.0, 'yp': 0.0 }  # 20% uneven triangle
}

ams_template = """AMS 1
Generate MultiCycleFM
BaseNote {0}
RootKey {0}
SampleRate 44100
Channels 1
BitsPerSample 16
Volume Auto"""

def compute_harmonic(number, params):
    n = float(number)
    a = params['a']
    b = params['b']
    c = params['c']
    x = n * math.pi * params['xp']
    y = n * math.pi * params['yp']
    d = params['d']
    e = params['e']
    module1 = 1.0 / math.pow(n, a)
    module2 = math.pow(math.sin(x), b) * math.pow(math.cos(x), c)
    module3 = math.pow(math.sin(y), d) * math.pow(math.cos(y), e)
    return module1 * module2 * module3

def get_harmonic_level(number, params, max_level = 1000.0): 
    a_max = 1.0
    a = compute_harmonic(number, params)
    v = math.log(abs(a / a_max))
    level = float(max_level) + 8.0 * v
    if level < 0:
        return 0.0
    return level

def get_harmonic_levels(waveform_name, count, max_level):
    params = waveform_params[waveform_name]
    levels = []
    n = 0
    while n < count:
        levels.append(get_harmonic_level(n + 1, params, max_level))
        n += 1
    return levels

if __name__ == '__main__':
    print(ams_template.format(69, 69))

    levels = get_harmonic_levels('pluckedString', 64, 1000.0)
    for i, l in enumerate(levels):
        print('Sine {0} {1}'.format(i + 1, l))

