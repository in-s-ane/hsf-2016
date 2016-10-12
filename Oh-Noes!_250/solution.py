# Public Function GetStringFromArray(fromArr() As Variant, LenLen As Integer) As String
#     Dim i As Integer
#     Dim result As String
#     result = ""
#     For i = LBound(fromArr) To UBound(fromArr)
#         result = result & Chr(fromArr(i) - LenLen + i * 2)
#     Next i
#     GetStringFromArray = result
# End Function
def get_string_from_array(from_arr, lenlen):
    result = ""
    for i in range(len(from_arr)):
        result = result + chr(from_arr[i] - lenlen + i * 2)
    return result

Professor = [148, 158, 156, 150, 94, 81, 79, 145, 79, 72, 121, 131, 117, 140, 127, 124, 109, 129, 123, 52, 103, 113, 109, 45, 106, 115, 109, 35, 93, 96, 86, 93, 95, 79, 75, 21, 71, 85, 65, 85, 10, 63, 80, 59]

print get_string_from_array(Professor, 44)

# From the zip, we get a word document, but it doesn't appear to contain anything visible.
# A little bit of digging around reveals the presence of VBA macros, which we can extract with olevba.py (see olevba.dump)
# Looking into the extracted VBA, we find an array of numbers called "Professor"

# We can also see that a function "GetStringFromArray" is being run on this array, so let's try and figure out what it does.
# This python code replicates the functionality of the original code, and when ran produces the following url:
# http://s3.amazonaws.com/nyu-infosec/csaw.exe

# Running the exe tells us the following:
# csaw.exe tells us the flag is in csaw2.exe though...

# http://s3.amazonaws.com/nyu-infosec/csaw2.exe
# Running that, we get "w1nterf3ll"
# Flag: w1nterf3ll
