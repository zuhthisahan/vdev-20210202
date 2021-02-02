import sys

print("### Building permit info for placer country ###")
if len(sys.argv) == 1:
    print("Please Enter a parcel number to search for ")
    print("For Example: 042-032-015-000")
else:
    print("Parcel number: " + str(sys.argv[1]))
    print("Looking up, building permits...")
