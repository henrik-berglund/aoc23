import setuptools.config.pyprojecttoml


def test1():
    i = 0

    while True:
        c1 = (i-52) % 53 == 0
        c2 = (i-66) % 67 == 0
        c3 = (i-72) % 73 == 0
        c4 = (i-58) % 59 == 0
        c5 = (i-46) % 47 == 0
        c6 = (i-78) % 79 == 0

        # i = 56787204940
        if c1 and c2 and c3 and c4 and c5 and c6:
            print(i)
            exit(0)
        i+= 1

def test2():

    schema = [52, 66, 72, 58, 46, 78]

    series = [set(), set(), set(), set(), set(), set()]
    for i, sc in enumerate(schema):
        scount=0
        for multiple in range(1000000000):
            new_num = schema[i]+ (schema[i]+1)*multiple
            if i == 0:
                series[i].add(new_num)
                scount+= 1
            elif i > 0 and new_num in series[i-1]:
                series[i].add(new_num)
                scount+= 1
        print(f"Schema {i} setup, {scount} nums", flush=True)

    print(sorted(series[5]))

#test2()


def generator(schema):
    num = schema
    yield num
    while True:
        num += schema+1
        yield num


def test3():
    schema = sorted([52, 66, 72, 58, 46, 78])

    gs = []
    for i in schema:
          gs.append(generator(i))

    state = []
    for i, g in enumerate(gs):
        state.append(next(g))

    num = state[0]
    while True:
        found = True
        for sc in range(2):
            if num == state[sc]:
                print(f"ok: {sc} {state}" )
                pass # all good so far
            elif num < state[sc]:
                print(f"nok: {sc} {state}" )
                found = False
                break
            else:
                while num > state[sc]:
                    state[sc] = next(gs[sc])
                if num != state[sc]:
                    found = False
                    print(f"nok2: {sc} {state}")
                    break
                print(f"ok2: {sc} {state}" )

        if found:
            print("found: ", state)

test3()

