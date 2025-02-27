
ciphered = "xbamvmlbtqspfuslssmsaeehzsmgwsyuwkwqljgpmelckmpyebfmsfcjyyhspnfsqeqsweyidjsbstzslmriyimkejzssnspejuysfefnceqljgpmelckmpyebfyvidqwrmzlbkqiqmmwgesatisixtozykeyigywiwfacwinpfqiufffriqpolcippjlmsvpthcxmgphpiwtewlxiobbsrxlowesgtpmasqldvsyqldgphsabjyegznhmwmzeshyrebvcjvphmcwmlrmcippjlytiwbsqwixcdcmepbkqmqldglxinfmasqfnshyrebumrwejlsheapjcpixffrswophqihldvsgeobmkgsxpkcytpmgsvsprmcksgfjlsyofmkejzseykpzcsjqiyuwnswtuateeeosqippjwquyptwpiewjryvexowqwilogcsroffyxycbdkirefgnwildvsgsydgpvicbeasqwjkrewashpmedogbsqtoymrstuwytwldglxerfebswgplmwgzokrexzvkcuypnsgwyxbncdsatyyrllwsywiwfacwwpneymscjsyfwzmmrevlqabeqpolciresspeqpnumrxldlmgsxbubygznmkegzoncvwlegrmtzdskevlesqsrztkmegzsvmhycbfriiduwquylujmerztumvvpvtcqtpmgoyizewtiqztjcihtusptecbgqtvijemwufblpseypkniplqspxiobubylzvncegzsvmviwblgzexffrieptkytvzqgqxeafdmuyptwnirdbnyuypbkqmqtsayegzolcgicogcrxlolmrecfumrxlhwkhsdwgrswbvwlsvxbdkirefkcjekdglwxlugswibvwyjmybdmtwejffeexbamvmlbtqspfuslsqpswasvopsqvekfkkewsbtgxylmecrxpfkrewlmlcveptvczixtwyzsepkkepnmsqwmqjuyhsdpmnsvbvwqsgzokghicbvmwrfmgqihpqggwhpddyveopktpmopkmytzsisigzolyfmwjryhsdognevejvmivcbvmeenpftivdbeshsfphqhitygshinpfregebjmwglnspehltvyghffsniwlsvyibafjgrgtbhmwmejnyhsxbfbexzbfrivtpjyglzvhmvfpnumrwejlsmvfnshyrebvcjvphmcwmlnglsgzmgpetposqgsxfdcmxztkmgmlmaqxedfkreiiqwpmrnjsoyilqwqevofslihejuyeyeolggexpkrvemfemuypfkriqupymredqjvmqltwjimptdckmdmsrmzlttcqwpjisieywwjrenjgleppbgasresjgshzrmcegzolcgiybkdvirvwqmedogfsygfsasvopkbikzwwprezowklsfwweszpsfyrxptvcsyesgqtecuabswbvwlshzqkkewypxsrhzfsniwlsvywjlmallednslwedrmcereoamgsdusriqlegrehzogqpxtngqxixqgqhmkffbsuffalhiaffbirefecrxpegqvidvdrehztnymhtbdmkecnmgxsprmcewapdrmgltkckytesqrsdmlgqsdbfmwwzqspetcpkqikfjjrshztkyfixpkoyinbkmstduwllexbamvmlbtqspfusmhmddgkyhlswmtwqbjmuyptwktvpgwxibnfgbiwebdckmdmsryvlfecwqzbumqvpdsbewzvkcnerpncvrlsvgvitusnsvttkmwixbvkmvlpisizpngqtscfpcqtwpgnexcpvmwtlujcwelgapqecrmctvpgwpiyxhgtivypvcqetpjgeemtgjyxlegnwsfrmczixpkpymcjgbiwpthcveopsrirebjgrzpslcveeffbrgtbvczseplgphpfdcmxzswqhsatvlstdqgpuypfkriwdbtcrhzrmcswpvhyvxteglsklozytvpgwpiqfnskemzsayefdpdsxeophqhsbvwmhityspgsyeaamsybvmiwbvwpheptwyhmcfarezzusrmpyphqesdfdcmxzswqhiptisivobkjlidswqxegplyvixuajredggpewdvscwuffjbe"

MAX_SUBSTRING_SIZE = 5
MIN_SUBSTRING_SIZE = 3
MAX_FACTOR = 30  #max key size


def main():
    get_pass_statistics(ciphered)
    

def get_pass_statistics(ciphered):
    print("factor X -> N words")
    big_ls = get_substrings_all_shifts(ciphered)
    substrings_factors = factorize_all(big_ls)

    all_factors = []
    for i in range(2, MAX_FACTOR + 1):
        all_factors.append(i)
    
    statistics = []
        
    maxi = 0
    max_prime = 0
    for a in all_factors:
        k = 0
        for b in substrings_factors:
            if(b == a):
                k = k + 1
                
        statistics.append((a, k))

    sorted_by_second = sorted(statistics, key=lambda tup: tup[1], reverse=True)
        
    for (a, b) in sorted_by_second:
        print(a, "->", b)
        


#returns all tuples (substring, spacing-in-between) for all substrings found repeated in the ciphered text
def get_substrings_all_shifts(ciphered): #as we shift the text different substrings will appear
    shifted = shift_right(ciphered)
    big_ls = []
    i = 1
    while(ciphered != shifted):
        ls = get_substrings(ciphered, shifted, i)
        big_ls.extend(ls)
        shifted = shift_right(shifted)
        i = i + 1
    return big_ls

        
#gets the tuples (substring, spacing-in-between) for the ciphered text and one of it's shifts
def get_substrings(ciphered, shifted, shift):
    ls = []
    for i in range(len(ciphered)): 
        #print("--->", i)
        k = 0
        str = ""
        while k in range(0, MAX_SUBSTRING_SIZE) and (i + k < len(ciphered)) and (ciphered[i + k] == shifted[i + k]):
            #while we detect a substring keep going
            str = str + ciphered[i + k]
                        
            if k >= MIN_SUBSTRING_SIZE - 1: #we are counting with the 0
                #we dont want short or null substrings
                pair = (str, shift)
                ls.append(pair)

            k = k + 1
    return ls


#shifts the ciphered text right
def shift_right(ciphered_text):
    li = list(ciphered_text)
    last = li.pop()
    li.insert(0, last)
    str = ''.join(li)
    return str


#factorizes the spacing-in-between for all substrings and returns all factors in a list
def factorize_all(big_li):
    all_factors = []
    for (a,b) in big_li:
        li = factorize(b)
        all_factors.extend(li)
    return all_factors
        

        
#returns the list os factors of a number
def factorize(number):
    ls = []
    for i in range(2, number):
        if(number % i == 0):
            ls.append(i)
    return ls


if __name__== "__main__":
    main()

