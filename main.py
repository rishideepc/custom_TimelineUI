import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root= customtkinter.CTk()
root.geometry("500x500")
selection= customtkinter.StringVar()

def generate_timeline():
    print("Test")

frame1 = customtkinter.CTkFrame(master=root)
frame1.pack(pady=20, padx=60, fill="both", expand=True)

label= customtkinter.CTkLabel(master=frame1, text="Py-Timeline Generator", font=('Roboto', 24))
label.pack(pady=15, padx=10)

entry1= customtkinter.CTkEntry(master=frame1, placeholder_text="Keyword", corner_radius=20)
entry1.pack(pady=12, padx=10)

entry2= customtkinter.CTkEntry(master=frame1, placeholder_text="Time Window", corner_radius=20)
entry2.pack(pady=12, padx=10)

entry3= customtkinter.CTkEntry(master=frame1, placeholder_text="Location", corner_radius=20)
entry3.pack(pady=12, padx=10)

button= customtkinter.CTkButton(master=frame1, text="Submit", command=generate_timeline(), corner_radius=10)
button.pack(pady=12, padx=10)

button= customtkinter.CTkButton(master=frame1, text="Generate Timeline", command=generate_timeline(), corner_radius=10)
button.pack(pady=12, padx=10)

frame2= customtkinter.CTkFrame(master=root)
frame2.pack(pady=20, padx=60, fill="both", expand=True)

card1= customtkinter.CTkTabview(master=frame2, text_color="blue")
card1.pack(pady=12, padx=10)


root.mainloop()


