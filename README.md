# Home Assistant Client

If you want a very simple client for your Home Assistant installation which reads some values
and outputs them in a formatted way, this is for you. Basically this is how it works:

1. Checkout this project to your computer (or just copy `main.py` and `config-template.ini`).
2. Copy `config-template.ini` to `config.ini` and edit it so it contains your Home Assistant login data,
   the requests you want the script to make and the formatted output containing the values.
3. Install the dependencies, e.g. by executing `pip3 install -r requirements.txt` (possibly inside a venv).
4. Call `main.py` with at least Python 3.2 installed (possibly inside the same venv).

## Example

When using the formatted output from `config-template.ini`, this is what the script could print
(given Home Assistant has the configured devices and parameters):

```
Temperature: 23.5 °C
Humidity: 47 %
```

## Notes regarding the output configured in `config.ini`

- If you want multiline output, you have to indent the second to the last line by 4 spaces each.
- You can include Python snippets inside the curly braces if you want (example in `config-template.ini`).
