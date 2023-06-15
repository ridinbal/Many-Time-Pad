
# Functions start here

# Function to find XOR values, it returns the result in Hex String
def xor_func(m1, m13):
    xor_hex_value = hex(m1 ^ m13)
    return xor_hex_value

# Function to convert the above-found Hex String to Binary
def hex_to_binary_func(xor_hex_value):
    hex1 = xor_hex_value[2:]
    binary_value = bin(int('1' + hex1, 16))[3:]
    return binary_value

# Function to convert the above Binary to ASCII
def toString(binaryString):
    return "".join([chr(int(binaryString[i:i + 8], 2)) for i in range(0, len(binaryString), 8)])

# Function to convert 8 bits at a time to ASCII and store it
def ascii_convertor_func(binary_value):
    mystring = ""
    store_value = ""
    list1 = []
    i = 0
    # print("Printing 8 bits of Binary:")

    for x in binary_value:

        mystring = mystring + x

        # Converting 8 bits to ASCII
        if len(mystring) >= 8:
            store_value = toString(mystring)

            list1.append(store_value)

            i = i + 1

            mystring = ""

    return list1

# Function to print the stored ASCII Values
def print_ascii_func(list0):
    print("Printing the stored ASCII Values")
    i = 0
    for x in list0:
        i = i + 1
        print(i, x)

# End of Functions

# Main Program starts here

# Storing All Messages

# We trimmed Messages 1 to 12 to match the length of Message 13
m1 = 0x0f351c71e76f5fbe548d4c54a69a2bcb3d2e4ceb3cfb5250c24dff419949683f8ed3a5f04f57116fe797410d2c138b60db6da534a7abe0f658b65b5c0ccbeb67d1c9d9216d8befeb35173f3596f40d4fa84e1e702818fbc06bec90d4315fceacfa7112c3e5 #5d74aaf3394bb08f7504a8e5019c4e3e838e0f364946f31721a49ad2d24ff6775efcb4f79fe4217a01b43cb5068bf3b52ca76543187274
m2 = 0x1a311571ff660da658c80545e98325ca646746a22ef55202d04cf90d93067c70a6c8b6b94c161120af95421b3a138b609d6abe2ae6b2e6eb42f7431405c4a56ad1c9cf3b67cafbe72301393583e80d58a34517767b19b58166a0c3db304acfbafa721591ea #4d398af07c49b69a7118fcff4889597aca81433b4953f50b2bbbdf9dcd0aff7013d3b5a3d3ec2b73019c3aa91b8bddf411a72b480c636cc6597494151386
m3 = 0x0f381a39fe6f41bd57c44646eacc3ecb2b695ae729ee174ac650ab0c92547a73b19ca7a24d40162bea9c0d1c2c1395678f6dec2ae8b4eaa449b1511507c3e06dd6c9c02c69c5eca4241d3f3585f44440ad011078381bacc075e4c3db304acfbafa721591ea
m4 = 0x0f351c71d96e59b742c34053a6853d9930664da237f24456874ae61198546b7ea6c8f7a34b581823ead8490c29568e618b68a929f3e6e6ea0ca35f1944c2ec70d686df3028c4f9a42a0720748cbb4e41a74c07773213bad56eefde922d44cdbcbf3e008be8 #0870a5eb7c55ab907f18fcf347dd433bcf83432d0849e80c22b0
m5 = 0x127d183cb07342a042d40553e9cc3dd83d2e5cea3be91756cf46f904d74f6c3fbcd3b8f04f431c27af8842003147c27a9425b82fe2e6f8ed5fb2540e05c9ee23d681cc3d28c7f6e227522466c2fe555aa34f116d7b1fb58168f4d8d72c0dd3b3bb701197fe #087baefe784eac9c3002b4f9488f0029c08606341d49ef113ff7cdd8c60abe6f5cefbff792e9317e4f9d36b948dfddf409e264580f65
m6 = 0x1835183ce0614abc558d4c41a69521cc646f5ae77aee5247cc4ae506d752777ae8c8a5a5565e5f26fcd84f0c2b47877cdb71a426e9e6eea440be525c00cff166c19dc23b28e2eba4271c2e7a97e94c49af5252787b1dbacf27f4df923c4883baa26e158dfe #416faebd7c4dba973004b9ff4a914529d0cf1432004cf94520bedf9dd00aea6750e9b5a580ad266d44de3cb304d295f447a1634c117a68c41e67d50d09c35928a62e6d6648371b40ac83b274cecb04d6c41b6fba
m7 = 0x1928103df46943b510d94044ee8227da256208f123ee4347ca50ab0899507073bed9a4f043161320fbd8420f7f5b837c9f25bb28f5adafe542b3170f14cfe66ac385c4336dcfbfef2c1d3a7987ff4a4bea4d13773c05bac662f390d3304983afa871008cee #4775b8bd7a54bb907e11fcfd4f99003ec68d163d0e49f2026ca3dfcec006f06513fcb4b3d3ff2279409d27b21ac2dbf2
m8 = 0x12290a71f96d5dbd43de4c45ea896ecd2b2e45ed2cf81756c803e70881433f6ba79cb8a047441e3bead84c1d7f528c77db69a931e2aaaff345a35f1311dea56fc788db2066ccbff030132e7091bb4f47be52526a3e15b6c869e7dccb7e40c6beb4771a84e1 #4d6ab8bd7f49be9e7d13b2e852dd4f3c839f06281a4ff20420f7d3d3d200ec6f52e9b3b89d
m9 = 0x0f351c71c7654ff251de056ea68920cf2d7d49e53ff9174bd303fc04d74e7e69ad9cb9bf56160c2aea960d002b139b6b8f25982fe2e6e9f158a2451944c3f623d19dc425648beceb621f38768abb4f47ad46176b7b04b3c069a0c4da3b0dd3bea96a54b7e4 #453989f86b55ba8b635b90f944
m10 = 0x127d0c22f5640da65f8d514fef822599306649f67afe4e40c251f81196457a3fbfdda4f0445f193bf6d8540c3e41912e9a72ad3ea791e7e558f77e5c10c2ea76c581d9697fcaeca4241b2b619bbb544bab5301393a07bad827f7d1c17e42cdb3a33e0086e3 #0860aefc6b48ff986717a5bc6093447ad487022e4969bc1124b8cfdadc1bbe7552eefaa396e36766449f21ae48cac2f41ee262595d616cd95963990b03824934ea2a287844722140b583a2638bcf16c3df0323a212740f3d5b517fbd10e4e253512e
m11 = 0x0c385930e2650da658c80544ee8522dd366b46a235fb17438757ee029f487073a7dbbeb3435a5f2ee89d0d3e3a138a6f8d60ec21e8b3e1e00ca4430e01cbe86fcb87c82d28dcfefd31522273c2ff4247a44652742e13b38168e690dd2b5f83adb56b008ae3 #4d39bcf26b50ffa9621fb2e84893477aca9c43340600f00a22b0dfcf941bf66713f2b4bb8aad307e58de3cbb48d9d0e515ad6f581e7f63cd59609a160d900d1faf2329634f354814b793bc37c3d700d5c71271e30d740e7815516dbd1af8a344533fcb
m12 = 0x0829003df52058a155c90553e9cc2cdc646f46a233f34347d542e8159e49713faad9a3a74753116ffb90484937468f6f9525bf28f2aaafe542b317080bc5e970829dc5287c8be8e130176d798bf6445aa34f1539121efbd56fe590d6374acaabbb725486ff #4939a2e9394cb6957c56b4fd5798002ecccf00350445bc033eb8d79dc007fb2240f2afbbd3ec2b704f9b

m13 = 0x14331c71fd614eba59c34007e58d2099206108f632f81755c851e04198403f79a1daa3a902590d2be6964c1b26138f6b95258228a7abeee744be591944c9e46d828dc2697cc3faa4351d3f7ec2f44b0ea54f17393e08afd366efc2d63743c2ada33e1982e3

list_m1 = []
list_m2 = []
list_m3 = []
list_m4 = []
list_m5 = []
list_m6 = []
list_m7 = []
list_m8 = []
list_m9 = []
list_m10 = []
list_m11 = []
list_m12 = []

# Storing All Messages
list_holder1 = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]

# Storing all ASCII Values
list_holder2 = [list_m1, list_m2, list_m3, list_m4, list_m5, list_m6, list_m7, list_m8, list_m9, list_m10, list_m11, list_m12]

list_holder3 = []

for i in range(0, 12):
    # Calling the XOR Function
    xor_hex_value = xor_func(list_holder1[i], m13) ##List_holder1 is a list that contains all messages and each messages XOR'd with message 13 using hex_function and the value is stored in xor_hex_value
    print("Hex value of Message", i + 1, "XOR'd with Message 13:")
    print(xor_hex_value + "\n")

    # Calling the Hex String to Binary Function
    binary_value = hex_to_binary_func(xor_hex_value)
    print("Binary of Message", i + 1, "XOR'd with message 13:")

    # Adding four 0's to the Binary of XOR'd Hex's of messages 1, 4, 5, 6, 7, 9
    # because all these messages start with 1 instead of 0
    if(i == 1 or i == 4 or i == 5 or i == 6 or i == 7 or i == 9):
        binary_value = "0000" + binary_value
        print(binary_value + "\n")
        list_holder3.append(binary_value) #Storing binary values to list_holder3

    else:
        print(binary_value + "\n")
        list_holder3.append(binary_value) #Storing binary values to list_holder3

    print("---------------------------------------------------------------------------------------------------------------" + "\n")

    # Binary to ASCII
    for k in range(0, len(list_holder3)):
        # Converting each Binary in list_holder3 to ASCII and storing in list_holder2
        list_holder2[i] = ascii_convertor_func(list_holder3[i])

# Each element in the list_holder2 is copied to their respective individual lists
list_m1 = list_holder2[0]
list_m2 = list_holder2[1]
list_m3 = list_holder2[2]
list_m4 = list_holder2[3]
list_m5 = list_holder2[4]
list_m6 = list_holder2[5]
list_m7 = list_holder2[6]
list_m8 = list_holder2[7]
list_m9 = list_holder2[8]
list_m10 = list_holder2[9]
list_m11 = list_holder2[10]
list_m12 = list_holder2[11]

# Printing ASCII
print("ASCII for each Message is as follows:\n")
print("Message 1: ", list_m1,"\n")
print("Message 2:", list_m2,"\n")
print("Message 3:", list_m3,"\n")
print("Message 4:", list_m4,"\n")
print("Message 5:", list_m5,"\n")
print("Message 6:", list_m6,"\n")
print("Message 7:", list_m7,"\n")
print("Message 8:", list_m8,"\n")
print("Message 9:", list_m9,"\n")
print("Message 10: ", list_m10,"\n")
print("Message 11: ", list_m11,"\n")
print("Message 12: ", list_m12)

# Key Finder program starts here
store_val = []
key_1 = [] #For storing alphabets after filtering out symbols
real_key = [] #For storing the actual key values

# Alphabet list
alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
              "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
              "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Finding key from ASCII
for i in range(0, 101):  # the number of rows it needs to iterate
    store_val.append(list_m1[i].lower())
    store_val.append(list_m2[i].lower())
    store_val.append(list_m3[i].lower())
    store_val.append(list_m4[i].lower())
    store_val.append(list_m5[i].lower())
    store_val.append(list_m6[i].lower())
    store_val.append(list_m7[i].lower())
    store_val.append(list_m8[i].lower())
    store_val.append(list_m9[i].lower())
    store_val.append(list_m10[i].lower())
    store_val.append(list_m11[i].lower())
    store_val.append(list_m12[i].lower())
    store_val = list(dict.fromkeys(store_val))  # removes duplicates

    for j in range(0, len(store_val)):
        if store_val[j] in alphabet_list:  # Checking if the store_val List has Alphabets
            key_1.append(store_val[j])     # If the List has Alphabets then Append it to the key_1

    if len(key_1) == 1:  # If the key_1 List has only 1 Alphabet then Append it to real_key list
        real_key.append(key_1[0])
    else:
        real_key.append("Space")  # If it has more than 1 alphabet then print Space

    store_val.clear()  # Clearing the values stored in the List before moving to the next row
    key_1.clear() # Clearing values stored in key_1 list before moving to the next row

# Printing the real_key/secret Message
print()
print("The Key/Secret Message is as follows: ")
print(real_key,"\n")
print("The Key/Secret Message Vertically: ")
for i in range(0, len(real_key)):
    print(i, real_key[i])

# Printing the complete Secret Message
print()
print("Secret Message is as follows: ")
print("One machine can do the work of fifty ordinary men; no machine can do the work of one extraordinary man")