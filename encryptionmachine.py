import flet as ft
import pyperclip

def main(page):
    page.title = "Encryption Machine"
    page.window_width = 500
    page.window_height = 500
    page.padding = 20

    def morse(text, do_encrypt):
        morse_code = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', ' ': '//'
        }
        
        if do_encrypt:
            result = []
            for letter in text.upper():
                if letter in morse_code:
                    result.append(morse_code[letter])
            return ' '.join(result)
        else:
            reverse = {v:k for k,v in morse_code.items()}
            result = []
            for code in text.split():
                if code in reverse:
                    result.append(reverse[code])
            return ''.join(result)

    def letters_to_numbers(text, do_encrypt):
        if do_encrypt:
            result = []
            for letter in text.upper():
                if letter.isalpha():
                    result.append(str(ord(letter) - 64))
            return ' '.join(result)
        else:
            result = []
            for num in text.split():
                if num.isdigit():
                    result.append(chr(int(num) + 64))
            return ''.join(result)

    def polar_cenit(text, do_encrypt):
        swap = {'P':'C', 'O':'E', 'L':'N', 'A':'I', 'R':'T',
                'C':'P', 'E':'O', 'N':'L', 'I':'A', 'T':'R'}
        result = []
        for letter in text:
            if letter.upper() in swap:
                new_letter = swap[letter.upper()]
                result.append(new_letter.lower() if letter.islower() else new_letter)
            else:
                result.append(letter)
        return ''.join(result)

    input_box = ft.TextField(label="Type your message here", multiline=True)
    output_box = ft.TextField(label="Secret message will appear here", multiline=True, read_only=True)
    
    method_choice = ft.Dropdown(
        options=[
            ft.dropdown.Option("Morse Code"),
            ft.dropdown.Option("Letters to Numbers"),
            ft.dropdown.Option("Polar Cenit"),
        ],
        value="Morse Code"
    )

    def encrypt(e):
        if not input_box.value:
            output_box.value = "Type something first!"
            page.update()
            return
            
        method = method_choice.value
        text = input_box.value
        
        if method == "Morse Code":
            output_box.value = morse(text, True)
        elif method == "Letters to Numbers":
            output_box.value = letters_to_numbers(text, True)
        elif method == "Polar Cenit":
            output_box.value = polar_cenit(text, True)
        
        page.update()

    def decrypt(e):
        if not input_box.value:
            output_box.value = "Type something first!"
            page.update()
            return
            
        method = method_choice.value
        text = input_box.value
        
        if method == "Morse Code":
            output_box.value = morse(text, False)
        elif method == "Letters to Numbers":
            output_box.value = letters_to_numbers(text, False)
        elif method == "Polar Cenit":
            output_box.value = polar_cenit(text, False)
        
        page.update()

    def copy_result(e):
        if output_box.value:
            pyperclip.copy(output_box.value)
            page.snack_bar = ft.SnackBar(ft.Text("Copied!"))
            page.snack_bar.open = True
            page.update()

    page.add(
        ft.Text("Secret Message Tool", size=24, weight="bold"),
        method_choice,
        input_box,
        ft.Row([
            ft.ElevatedButton("Encrypt", on_click=encrypt),
            ft.ElevatedButton("Decrypt", on_click=decrypt),
        ]),
        output_box,
        ft.ElevatedButton("Copy to Clipboard", on_click=copy_result),
    )

ft.app(target=main)