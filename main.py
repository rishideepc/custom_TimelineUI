import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root= customtkinter.CTk()
root.geometry("500x500")
selection= customtkinter.StringVar()

def generate_timeline():
    print("Test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label= customtkinter.CTkLabel(master=frame, text="Py-Timeline Generator", font=('Roboto', 24))
label.pack(pady=15, padx=10)

entry1= customtkinter.CTkEntry(master=frame, placeholder_text="Keyword", corner_radius=20)
entry1.pack(pady=12, padx=10)

entry2= customtkinter.CTkEntry(master=frame, placeholder_text="Time Window", corner_radius=20)
entry2.pack(pady=12, padx=10)

entry3= customtkinter.CTkEntry(master=frame, placeholder_text="Location", corner_radius=20)
entry3.pack(pady=12, padx=10)

button= customtkinter.CTkButton(master=frame, text="Submit", command=generate_timeline(), corner_radius=10)
button.pack(pady=12, padx=10)

button= customtkinter.CTkButton(master=frame, text="Generate Timeline", command=generate_timeline(), corner_radius=10)
button.pack(pady=12, padx=10)


root.mainloop()


