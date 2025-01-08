import sys
import subprocess


def run_tests():
    try:
        subprocess.run([sys.executable, "-m", "pytest", "tests/"], check=True)
        print("\n All tests passed correctly. \u2714")
    except subprocess.CalledProcessError:
        print(
            """
              \n Some tests failed. Check the output for more details. \u274C
              """
        )
        sys.exit(1)


if __name__ == "__main__":
    run_tests()
