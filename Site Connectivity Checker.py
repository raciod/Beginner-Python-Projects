import urllib.request as urllib


def main(url):
    print("Checking connectivity...")
    try:
        response = urllib.urlopen(url)
        print("Connecter to " , url , "Succesfuly")
        print("The response code was" , response.getcode())
    except Exception as e:
        print("Connection to", url, "failed:", str(e))

print("This is a site connectivity ckecker program")
input_url = input("Input the url of the site you want to check: ")

main(input_url)