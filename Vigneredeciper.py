from collections import Counter

def find_the_coincidence(file_path):
    try:
            with open(file_path, 'r') as file:
                content = file.read()
            
            frequency={}
            for i in range(100):
                coincidence=0
                for j in range(len(content)-i):
                    if content[j]==content[j+i]:
                         coincidence+=1
                frequency[i]=coincidence
            
            return frequency
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

def probable_key_finder(file_path, key_length):
    try:
            with open(file_path, 'r') as file:
                content = file.read()
            
            key=[]
            fragments=[[] for _ in range(key_length)]
            for i in range(len(content)):
                fragments[i%key_length].append(content[i])

            
            for i in range(key_length):
                frequency=Counter(fragments[i])
                char=max(zip(frequency.values(), frequency.keys()))[1]
                
                if(ord(char)>ord('e')):
                    key.append(chr(97 + (ord(char) - ord('e'))))
                else:
                    key.append(chr(97 + 26+(ord(char) - ord('e'))))
            return key
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

def decoder(file_path,key,key_length,output_path):
    try:
            with open(file_path, 'r') as file:
                content = file.read()
            
            key_map=[ord(ch) for ch in key]
            new_content=""
            for i in range(len(content)):
                temp=ord(content[i])-key_map[i%key_length]
                if (temp>=0):
                    new_content+=chr(temp+97)
                else:
                    new_content+=chr(temp+97+26)
            
            with open(output_path, 'w') as file:
                file.write(new_content)
            
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
     
file_path="v_ciphertext_70.txt"
frequency=find_the_coincidence(file_path)
print(frequency)

key_len=7
key =probable_key_finder(file_path,key_len)
print(key)

out_path="vignereDecipher.txt"
decoder(file_path,key,key_len,out_path)
