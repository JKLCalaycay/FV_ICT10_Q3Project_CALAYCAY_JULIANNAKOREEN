
from pyscript import document # pyright: ignore[reportMissingImports]
#maam theres something wrong with my vsc when i remove the comment above so i used the quick fix button to fix it 😢 - Zoe

#this is where the functions are for account creation

def check_account(e):
    username = document.getElementById('user_name').value
    password = document.getElementById("pass_code").value
    output = document.getElementById('account_result')
    output.innerHTML = ""

    #these variables are used so that the main.py file knows what to call out (the codes here are from sw 2 and skillstest)

    if len(username) < 9:
        output.innerHTML = f"Username too short. Add {9 - len(username)} characters."
        return

    has_num = any(c.isdigit() for c in password)
    has_let = any(c.isalpha() for c in password) #this code is from the example you gave us po pero it didnt work initially so we asked ai for help

    if len(password) < 10:
        output.innerHTML = f"Password too short. Add {10 - len(password)} characters."
    elif not has_let:
        output.innerHTML = "Password needs a letter."
    elif not has_num:
        output.innerHTML = "Password needs a number."
    else:
        output.innerHTML = "Account made successfully! :)" #these are the if else statements that we used for the project. They basically check if the info they recieved is true for one of them

def check_eligibility(e):
    output = document.getElementById('elig_result')
    list_area = document.getElementById('player_list_area')
    list_title = document.getElementById('list_title')  #these are more variables so that the file knows what to call out 
    names_div = document.getElementById('names_display')

    
    output.innerHTML = ""
    list_area.style.display = "none"
    names_div.innerHTML = ""

    reg = document.getElementById('reg_yes').checked
    med = document.getElementById('med_yes').checked
    grade_val = document.getElementById('grade_lvl').value

    if not reg or not med:
        output.innerHTML = "Error: Check Registration/Medical status."
        return
    if grade_val == "":
        output.innerHTML = "Enter a grade level."  #so in this part maam we honestly got so lost that we asked ai what to do here because when we tried to use w3schools nothing helped us
        return

    grade = int(grade_val)

    if 7 <= grade <= 10:
        teams = {7: "Blue Bears", 8: "Red Bulldogs", 9: "Yellow Tigers", 10: "Green Hornets"} #Anyway, these codes are used to determine which team the applicant is in
        team = teams[grade]
        output.innerHTML = f"Eligible! Team: {team}"
        list_area.style.display = "block"

        if grade == 10:
            list_title.innerHTML = "Green Hornets Player List:"
            list_title.style.color = "#84fab0"
            players = ["Al Hazmi, Ebtisam", "Alvarez, Yaniszolt", "Belsa, Ethan", "Bernas, Giana", "Calaycay, Julianna", "Castelo, Jamilla", "Cruz, Francesca", "Defensor, Ely", "Dimasuhid, Danielle", "Francisco, Althea", "Hsu, Cristina", "Juatchon, Denise", "Judge, Judah", "Lilagan, Francis", "Luna, Sam", "Macaranas, Enzo", "Mateo, Pain", "Mondragon, Ashely", "Naldoza, Lance", "Natividad, Gabriel", "Ng, Sofia", "Ong, Hendrich", "Paz, Trisha", "Ramos, Miguel", "Ramos, Queeny", "Ramos, Samanntha", "Reodica, Ashlei", "Repolona, Vaughn"]
            
            for i, name in enumerate(players, 1):
                p = document.createElement("div") #we do not know how this works chatgpt just told us to put it here so that our code can work po..
                p.innerHTML = f"{i}. {name}"
                names_div.appendChild(p)
        else:
            list_title.innerHTML = "Player list is only for Grade 10."
    else:
        output.innerHTML = "Only Grades 7-10 are eligible."

#this button code is used to display the list of players using loops (for)
def display_players(event):
    # List of classmates
    players = [
        "Al Hazmi, Ebtisam Abdullah","Alvarez, Yaniszolt Aeiou Cabico", "Belsa, Ethan Drei San Miguel", "Bernas, Giana Zoe Palonpon", "Calaycay, Julianna Koreen Lingat", "Castelo, Jamilla Alynna Alvarez", 
        "Cruz, Francesca Meyer Uson", "Defensor, Ely Jr. Tica", "Dimasuhid, Danielle Luna Quibol", "Francisco, Althea Mauri Diaz", "Hsu, Cristina Wen Viray",
        "Juatchon, Denise Cristine Gamboa", "Judge, Judah Daniel San Juan", "Lilagan, Francis Geoffrey Cuaresma", "Luna, Sam Bernice Genabe", "Macaranas, Enzo Josh Palma", "Mateo, Pain Adler Garcia", "Mondragon, Ashely Nicole Tierra", "Naldoza, Lance Arthur Pacho",
        "Natividad, Gabriel Emilio Cabanayan","Ng, Sofia Pola Aldeguer", "Ong, Hendrich Mathis Del Rosario", "Paz, Trisha Lorainne Dacara",
        "Ramos, Miguel Christian Datu", "Ramos, Queeny Haraj Guilas", "Ramos, Samanntha Anne",
        "Reodica, Ashlei Lavigne Luz", "Repolona, Vaughn Matthew Ramos",
    ]
    
    output_div = document.getElementById("output")
    output_div.innerHTML = "" # Clears previous list to avoid duplication
    
    # Python Loop
    count = 1
    for name in players:
        # Create a new div for each player
        player_element = document.createElement("div")
        player_element.innerHTML = f"{count}) {name}"
        
        # Adds the result to the output area
        output_div.appendChild(player_element)
        count += 1

#GREEN HORNETS PRIDE