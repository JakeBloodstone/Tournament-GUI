import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import json

individual_data = []
team_data = []

# This function is called at the end of the code for the program to 'remember' the individuals registered
def load_individual_data():
    try:
        with open("individual_data.json", "r") as file:
            json_data = file.read()
            individual_data.extend(json.loads(json_data))
    except FileNotFoundError:
        # If File is not found, no individuals would have been registered at this point in time
        pass

# This function is called at the end of the code for the program to 'remember' the teams registered
def load_team_data():
    try:
        with open("team_data.json", "r") as file:
            json_data = file.read()
            team_data.extend(json.loads(json_data))
    except FileNotFoundError:
        # If File is not found, no teams would have been registered at this point in time
        pass

# This function was made to register a single individual to the "individual_data" list
def register_individual():
    individual_window = tk.Toplevel(window)
    individual_window.title("Register Individual")

    label_heading = tk.Label(individual_window, text="Individual Registration", font=("Arial", 16, "bold"))
    label_heading.pack(pady=10)

    def submit_registration():
        name = entry_name.get()
        individual = {"name": name, "score": 0}
        individual_data.append(individual)
        json_data = json.dumps(individual_data)
        with open("individual_data.json", "w") as file:
            file.write(json_data)
        messagebox.showinfo("Registration", "Individual registration successful!")
        individual_window.destroy()

    label_name = tk.Label(individual_window, text="Name:")
    label_name.pack()
    entry_name = tk.Entry(individual_window)
    entry_name.pack()

    button_submit = tk.Button(individual_window, text="Submit", command=submit_registration)
    button_submit.pack(pady=10)


def register_team():
    team_window = tk.Toplevel(window)
    team_window.title("Register Team")

    label_heading = tk.Label(team_window, text="Team Registration", font=("Arial", 16, "bold"))
    label_heading.pack(pady=10)

    def submit_registration():
        team_name = entry_team_name.get()
        team_members_input = entry_team_members.get().split(",")
        team_members = [{"name": member.strip(), "score": 0} for member in team_members_input]

        total_score = sum(member.get("score", 0) for member in team_members)

        # This prevents users from entering less than five team members
        if len(team_members) < 5:
            messagebox.showerror("Error", "There must be five members on a team")
            return

        # This prevents users from entering more than five members
        if len(team_members) > 5:
            messagebox.showerror("Error", "Maximum 5 Team Members are allowed on a team")
            return

        # This prevents users from entering duplicate team members
        if len(set(member["name"] for member in team_members)) != len(team_members):
            messagebox.showerror("Error", "Duplicate Team Members are not allowed!")
            return

        team = {"team_name": team_name, "team_members": team_members, "total_score": total_score}
        team_data.append(team)
        json_data = json.dumps(team_data)
        with open("team_data.json", "w") as file:
            file.write(json_data)
        messagebox.showinfo("Registration", "Team registration successful!")
        team_window.destroy()

    label_team_name = tk.Label(team_window, text="Team Name:")
    label_team_name.pack()
    entry_team_name = tk.Entry(team_window)
    entry_team_name.pack()

    label_team_members = tk.Label(team_window, text="Team Members (comma-separated):")
    label_team_members.pack()
    entry_team_members = tk.Entry(team_window)
    entry_team_members.pack()

    button_submit = tk.Button(team_window, text="Submit", command=submit_registration)
    button_submit.pack(pady=10)


def display_individuals():
    print("Individuals:")
    for individual in individual_data:
        print(f"- {individual['name']}: Score {individual['score']}")


def display_teams():
    print("Teams:")
    for team in team_data:
        print("Team Name:", team["team_name"])
        print("Team Members:")
        for member in team["team_members"]:
            print(f" - {member['name']}: Score {member['score']}")
        print("Total Score:", team["total_score"])
        print()


def assign_score_individual():
    name = simpledialog.askstring("Assign Score", "Enter the name of the individual:")
    if name:
        for individual in individual_data:
            if individual["name"] == name:
                score = simpledialog.askinteger("Assign Score", "Enter the score for the individual:")
                if score is not None:
                    individual["score"] = score
                    json_data = json.dumps(individual_data)
                    with open("individual_data.json", "w") as file:
                        file.write(json_data)
                    messagebox.showinfo("Score Assigned", "Score has been assigned to the individual.")
                break
        else:
            messagebox.showerror("Error", "Individual not found.")


from tkinter import simpledialog

def assign_score_team():
    name = simpledialog.askstring("Assign Score", "Enter the name of the team member:")
    if name:
        for team in team_data:
            for member in team["team_members"]:
                if member["name"] == name:
                    score = simpledialog.askinteger("Assign Score", "Enter the score for the team member:")
                    if score is not None:
                        member["score"] = score
                        team["total_score"] = sum(member.get("score", 0) for member in team["team_members"])
                        json_data = json.dumps(team_data)
                        with open("team_data.json", "w") as file:
                            file.write(json_data)
                        messagebox.showinfo("Score Assigned", "Score has been assigned to the team member.")
                    break
            else:
                continue
            break
        else:
            messagebox.showerror("Error", "Team member not found.")

def display_individuals():
    print("Individuals:")
    for individual in individual_data:
        print(individual["name"], "Score:", individual.get("score", 0))


def display_teams():
    print("Teams:")
    for team in team_data:
        print("Team Name:", team["team_name"])
        print("Team Members:")
        for member in team["team_members"]:
            print(f" - {member['name']}: Score {member['score']}")
        print("Total Score:", team["total_score"])
        print()


window = tk.Tk()

frame_register_individual = tk.Frame(window)
frame_register_individual.grid(row=0, column=0, pady=5)
label_register_individual = tk.Label(frame_register_individual, text="Register Individual")
label_register_individual.grid(row=0, column=0, sticky="nsew")
button_register_individual = tk.Button(frame_register_individual, text="Register", command=register_individual,
                                       relief=tk.RAISED, padx=10)
button_register_individual.grid(row=0, column=1, sticky="nsew")

frame_register_team = tk.Frame(window)
frame_register_team.grid(row=1, column=0, pady=5)
label_register_team = tk.Label(frame_register_team, text="Register Team")
label_register_team.grid(row=0, column=0, sticky="nsew")
button_register_team = tk.Button(frame_register_team, text="Register", command=register_team, relief=tk.RAISED, padx=10)
button_register_team.grid(row=0, column=1, sticky="nsew")

frame_display_individuals = tk.Frame(window)
frame_display_individuals.grid(row=2, column=0, pady=5)
label_display_individuals = tk.Label(frame_display_individuals, text="Display Individuals")
label_display_individuals.grid(row=0, column=0, sticky="nsew")
button_display_individuals = tk.Button(frame_display_individuals, text="Display", command=display_individuals,
                                       relief=tk.RAISED, padx=10)
button_display_individuals.grid(row=0, column=1, sticky="nsew")

frame_display_teams = tk.Frame(window)
frame_display_teams.grid(row=3, column=0, pady=5)
label_display_teams = tk.Label(frame_display_teams, text="Display Teams")
label_display_teams.grid(row=0, column=0, sticky="nsew")
button_display_teams = tk.Button(frame_display_teams, text="Display", command=display_teams, relief=tk.RAISED, padx=10)
button_display_teams.grid(row=0, column=1, sticky="nsew")

frame_assign_score_individual = tk.Frame(window)
frame_assign_score_individual.grid(row=4, column=0, pady=5)
label_assign_score_individual = tk.Label(frame_assign_score_individual, text="Assign Score to Individual")
label_assign_score_individual.grid(row=0, column=0, sticky="nsew")
button_assign_score_individual = tk.Button(frame_assign_score_individual, text="Assign Score",
                                           command=assign_score_individual, relief=tk.RAISED, padx=10)
button_assign_score_individual.grid(row=0, column=1, sticky="nsew")

frame_assign_score_team = tk.Frame(window)
frame_assign_score_team.grid(row=5, column=0, pady=5)
label_assign_score_team = tk.Label(frame_assign_score_team, text="Assign Score to Team Member")
label_assign_score_team.grid(row=0, column=0, sticky="nsew")
button_assign_score_team = tk.Button(frame_assign_score_team, text="Assign Score", command=assign_score_team,
                                     relief=tk.RAISED, padx=10)
button_assign_score_team.grid(row=0, column=1, sticky="nsew")

load_individual_data()

load_team_data()

window.mainloop()