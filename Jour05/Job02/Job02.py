def draw_rectangle(width, height):
    text = "-"
    text2 = "|"
    text3 = " "
    text_haut = " "
    text_haut += text2
    text3 += text2

    for i in range(width):
        text_haut += text
        text3 += " " 
    text_haut += text2


        

    text3 += text2

    print(text_haut)

    for i in range(height):
        print(text3)
    
    print(text_haut)
    




    


draw_rectangle(10,3)