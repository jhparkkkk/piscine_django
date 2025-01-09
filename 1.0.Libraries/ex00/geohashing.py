import sys
import antigravity


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Requires 3 arguments: latitude, longitude, date of the week")
    try:
        antigravity.geohash(float(sys.argv[1]), float(
            sys.argv[2]), sys.argv[3].encode())
    except Exception as e:
        print(e)
        exit(1)
