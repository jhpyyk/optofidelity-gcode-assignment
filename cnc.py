import sys

import Runner

def main(args):
    runner = Runner.Runner(args[1])
    runner.run_simulation()

if __name__ == "__main__":
    main(sys.argv)