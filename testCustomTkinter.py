import customtkinter
import tkinter

app = customtkinter.CTk()
app.geometry(f"{600}x{500}")
app.title("CTk example")
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# def button_event():
#     print("button pressed")
#
# button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_event)
# button.pack(padx=20, pady=10)

# button = customtkinter.CTkButton(master=app,
#                                  width=120,
#                                  height=32,
#                                  border_width=0,
#                                  corner_radius=8,
#                                  text="CTkButton",
#                                  command=button_event)
# button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# def slider_event(value):
#     print(value)
#
# slider = customtkinter.CTkSlider(master=app, from_=0, to=100, command=slider_event)
# slider.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


# # create scrollable textbox
# tk_textbox = tkinter.Text(app, highlightthickness=0)
# tk_textbox.grid(row=0, column=0, sticky="nsew")
#
# # create CTk scrollbar
# ctk_textbox_scrollbar = customtkinter.CTkScrollbar(app, command=tk_textbox.yview)
# ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")
#
# # connect textbox scroll event to CTk scrollbar
# tk_textbox.configure(yscrollcommand=ctk_textbox_scrollbar.set)

entry = customtkinter.CTkEntry(master=app, placeholder_text="CTkEntry")
entry.pack(padx=20, pady=10)

app.mainloop()