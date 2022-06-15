try:
    f = open("sample.txt", "w")
    f.write("Test write to sample file")

except:
    print("ERROR: Could not find or read data")
else:
    print("Success!")
    f.close()


try:
    f = open("sample.txt", "r")
    f.write("Test write to sample file")

except:
    print("ERROR: Could not find or read data")
else:
    print("Success!")
    f.close()
finally:
    print("This prints anyway")
