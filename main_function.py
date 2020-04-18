   
#assignment109 Main Function
if __name__ == "__main__":    
    userinput=input("Please type 'R' for Mirror/Reflection or 'T' for Threshold or 'S' for Saving file or 'q' to quit/exit: ")
    while userinput!='q':
        if userinput=='R':
            R=mirror("testimage.jpg")
            show_image(R)
            userinput=input("Please type 'R' for Mirror/Reflection or 'T' for Threshold or 'S' for Saving file or 'q' to quit/exit: ")
        elif userinput=='T':
            T=threshold("testimage.jpg")
            show_image(T)
            userinput=input("Please type 'R' for Mirror/Reflection or 'T' for Threshold or 'S' for Saving file or 'q' to quit/exit: ")
        elif userinput=='S':
            S=FileSavings(image_array)
            userinput=input("Please type 'R' for Mirror/Reflection or 'T' for Threshold or 'S' for Saving file or 'q' to quit/exit: ")
        elif userinput=='q':
            exit()
        else:
            userinput=input("Please type  R for Mirror/Reflection or T for Threshold or S for Saving file: ")