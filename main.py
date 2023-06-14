import tkinter as tk
from tkinter import messagebox
import json

individual_data = []
team_data = []
selected_individual = None
selected_team = None

def load_individual_data():
    global individual_data
    try:
        with open("individual_data.json", "r") as file:
            data = file.read()
            if data:
                individual_data = json.loads(data)
    except FileNotFoundError:
        pass

def load_team_data():
    global team_data

    try:
        with open("team_data.json", "r") as file:
            team_data = json.load(file)
            # Check if each team has the "members" key
            for team in team_data:
                if "members" not in team:
                    team["members"] = []
    except FileNotFoundError:
        team_data = []

def register_individual():
    individual_window = tk.Toplevel(window)
    individual_window.title("Individual Registration")

    label_heading = tk.Label(individual_window, text="Individual Registration", font=("Arial", 16, "bold"))
    label_heading.pack(pady=10)

    def submit_registration():
        name = entry_name.get()
        score = entry_score.get()

        individual = {"name": name, "score": score}
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

    label_score = tk.Label(individual_window, text="Score:")
    label_score.pack()
    entry_score = tk.Entry(individual_window)
    entry_score.pack()

    button_submit = tk.Button(individual_window, text="Submit", command=submit_registration)
    button_submit.pack(pady=10)

def register_team():
    team_window = tk.Toplevel(window)
    team_window.title("Team Registration")

    label_heading = tk.Label(team_window, text="Team Registration", font=("Arial", 16, "bold"))
    label_heading.pack(pady=10)

    def submit_registration():
        team_name = entry_team_name.get()
        team_members = entry_team_members.get().split(",")

        team = {"team_name": team_name, "members": team_members, "total_score": 0}
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

    label_team_members = tk.Label(team_window, text="Team Members (Comma-separated):")
    label_team_members.pack()
    entry_team_members = tk.Entry(team_window)
    entry_team_members.pack()

    button_submit = tk.Button(team_window, text="Submit", command=submit_registration)
    button_submit.pack(pady=10)

def display_individuals():
    individuals_window = tk.Toplevel(window)
    individuals_window.title("Registered Individuals")

    label_heading = tk.Label(individuals_window, text="Registered Individuals", font=("Arial", 16, "bold"))
    label_heading.pack(pady=10)

    for individual in individual_data:
        label_name = tk.Label(individuals_window, text=individual["name"])
        label_name.pack()

def display_teams():
    teams_window = tk.Toplevel(window)
    teams_window.title("Registered Teams")

    label_heading = tk.Label(teams_window, text="Registered Teams", font=("Arial", 16, "bold"))
    label_heading.pack(pady=10)

    for team in team_data:
        label_team_name = tk.Label(teams_window, text=f"Team Name: {team['team_name']}")
        label_team_name.pack()

        label_team_members = tk.Label(teams_window, text="Team Members:")
        label_team_members.pack()

        for member in team['members']:
            label_member_name = tk.Label(teams_window, text=member)
            label_member_name.pack()

        label_team_divider = tk.Label(teams_window, text="-----------------------------")
        label_team_divider.pack(pady=5)

def update_individual_scores():
    individuals_window = tk.Toplevel(window)
    individuals_window.title("Update Individual Scores")

    label_heading = tk.Label(individuals_window, text="Update Individual Scores", font=("Arial", 16, "bold"))
    label_heading.pack(pady=10)

    def submit_scores():
        name = entry_name.get()
        score = entry_score.get()

        for individual in individual_data:
            if individual["name"] == name:
                individual["score"] = score
                json_data = json.dumps(individual_data)
                with open("individual_data.json", "w") as file:
                    file.write(json_data)
                messagebox.showinfo("Score Update", f"Score updated for {name}")
                individuals_window.destroy()
                return

        messagebox.showerror("Error", f"No individual found with name: {name}")

    label_name = tk.Label(individuals_window, text="Name:")
    label_name.pack()
    entry_name = tk.Entry(individuals_window)
    entry_name.pack()

    label_score = tk.Label(individuals_window, text="Score:")
    label_score.pack()
    entry_score = tk.Entry(individuals_window)
    entry_score.pack()

    button_submit = tk.Button(individuals_window, text="Submit", command=submit_scores)
    button_submit.pack(pady=10)

def update_team_scores():
    teams_window = tk.Toplevel(window)
    teams_window.title("Update Team Scores")

    label_heading = tk.Label(teams_window, text="Update Team Scores", font=("Arial", 16, "bold"))
    label_heading.pack(pady=10)

    def submit_scores():
        team_name = entry_team_name.get()
        score = entry_score.get()

        for team in team_data:
            if team["team_name"] == team_name:
                team["total_score"] = score
                json_data = json.dumps(team_data)
                with open("team_data.json", "w") as file:
                    file.write(json_data)
                messagebox.showinfo("Score Update", f"Score updated for {team_name}")
                teams_window.destroy()
                return

        messagebox.showerror("Error", f"No team found with name: {team_name}")

    label_team_name = tk.Label(teams_window, text="Team Name:")
    label_team_name.pack()
    entry_team_name = tk.Entry(teams_window)
    entry_team_name.pack()

    label_score = tk.Label(teams_window, text="Score:")
    label_score.pack()
    entry_score = tk.Entry(teams_window)
    entry_score.pack()

    button_submit = tk.Button(teams_window, text="Submit", command=submit_scores)
    button_submit.pack(pady=10)

def assign_to_event():
    global selected_individual, selected_team

    assign_name = entry_assign_name.get().strip()
    event_individual = dropdown_individual.get()
    event_team = dropdown_team.get()

    if assign_name == "":
        messagebox.showerror("Error", "Please enter an individual/team name.")
        return

    if event_individual != "Select Event":
        individual = next((ind for ind in individual_data if ind["name"] == assign_name), None)
        if individual is None:
            messagebox.showerror("Error", "Selected individual not found.")
        else:
            individual[event_individual] = assign_name
            messagebox.showinfo("Success", "Individual assigned to event successfully.")
            selected_individual = None

    elif event_team != "Select Event":
        team = next((team for team in team_data if team["team_name"] == assign_name), None)
        if team is None:
            messagebox.showerror("Error", "Selected team not found.")
        else:
            team[event_team] = assign_name
            messagebox.showinfo("Success", "Team assigned to event successfully.")
            selected_team = None

    entry_assign_name.delete(0, tk.END)
    dropdown_individual.set("Select Event")
    dropdown_team.set("Select Event")

def assign_individual_or_team():
    global selected_individual, selected_team

    if selected_individual is not None:
        selected_event = dropdown_individual.get()
        if selected_event == "Select Event":
            messagebox.showerror("Error", "Please select an event.")
        else:
            messagebox.showinfo("Assign Individual", f"Event: {selected_event}\nIndividual: {selected_individual}")
            assign_name = selected_individual
            event = selected_event

            individual = next((ind for ind in individual_data if ind["name"] == assign_name), None)
            if individual is not None:
                individual[event] = assign_name
                messagebox.showinfo("Success", "Individual assigned to event successfully.")
            else:
                messagebox.showerror("Error", "Selected individual not found.")

            dropdown_individual.set("Select Event")
            selected_individual = None

    elif selected_team is not None:
        selected_event = dropdown_team.get()
        if selected_event == "Select Event":
            messagebox.showerror("Error", "Please select an event.")
        else:
            messagebox.showinfo("Assign Team", f"Event: {selected_event}\nTeam: {selected_team}")
            assign_name = selected_team
            event = selected_event

            team = next((team for team in team_data if team["team_name"] == assign_name), None)
            if team is not None:
                team[event] = assign_name
                messagebox.showinfo("Success", "Team assigned to event successfully.")
            else:
                messagebox.showerror("Error", "Selected team not found.")

            dropdown_team.set("Select Event")
            selected_team = None

window = tk.Tk()
window.title("Event Registration")

selected_event = tk.StringVar()

load_individual_data()
load_team_data()

label_heading = tk.Label(window, text="Event Registration", font=("Arial", 16, "bold"))
label_heading.grid(row=0, column=0, columnspan=3, pady=10)

button_register_individual = tk.Button(window, text="Register Individual", command=register_individual)
button_register_individual.grid(row=1, column=0, padx=10, pady=5)

button_register_team = tk.Button(window, text="Register Team", command=register_team)
button_register_team.grid(row=1, column=1, padx=10, pady=5)

button_display_individuals = tk.Button(window, text="Display Individuals", command=display_individuals)
button_display_individuals.grid(row=1, column=2, padx=10, pady=5)

button_display_teams = tk.Button(window, text="Display Teams", command=display_teams)
button_display_teams.grid(row=2, column=0, padx=10, pady=5)

button_update_individual_scores = tk.Button(window, text="Update Individual Scores", command=update_individual_scores)
button_update_individual_scores.grid(row=2, column=1, padx=10, pady=5)

button_update_team_scores = tk.Button(window, text="Update Team Scores", command=update_team_scores)
button_update_team_scores.grid(row=2, column=2, padx=10, pady=5)

label_assign_individual = tk.Label(window, text="Assign Individual to Event:")
label_assign_individual.grid(row=3, column=0, padx=10, pady=5)

dropdown_individual = tk.StringVar(window)
dropdown_individual.set("Select Event")
dropdown_individual.trace('w', lambda *args: assign_individual_or_team())
dropdown_menu_individual = tk.OptionMenu(window, dropdown_individual, "Reading", "Longest Cod", "Chicken Broth", "Biggest Trout", "Murder")
dropdown_menu_individual.grid(row=3, column=1, padx=10, pady=5)

label_assign_team = tk.Label(window, text="Assign Team to Event:")
label_assign_team.grid(row=4, column=0, padx=10, pady=5)

dropdown_team = tk.StringVar(window)
dropdown_team.set("Select Event")
dropdown_team.trace('w', lambda *args: assign_individual_or_team())
dropdown_menu_team = tk.OptionMenu(window, dropdown_team, "Reading", "Longest Cod", "Chicken Broth", "Biggest Trout", "Murder")
dropdown_menu_team.grid(row=4, column=1, padx=10, pady=5)

label_assign_name = tk.Label(window, text="Assign Individual/Team:")
label_assign_name.grid(row=5, column=0, padx=10, pady=5)

entry_assign_name = tk.Entry(window)
entry_assign_name.grid(row=5, column=1, padx=10, pady=5)

button_assign = tk.Button(window, text="Assign to Event", command=assign_to_event)
button_assign.grid(row=5, column=2, padx=10, pady=5)

window.mainloop()