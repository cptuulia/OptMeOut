# OptMeOut

## Install

1) Clone this repo.
2) Make sure that you have Python installed in your computer.
3) Make sure that you have read and write permissions in the following
   folders

```
src/csv/export/
src/csv/import/
src/languages/
dist/
dist/js
```

In Nix systems you do this

```
sudo chmod a+rw src/csv/export/
sudo chmod a+rw src/csv/import/
sudo chmod a+rw src/languages/
sudo chmod a+rw dist/
sudo chmod a+rw dist/js/
```

## Importing new languages

1) run the command

```
python build.py
```

2) In the folder ```src/csv/export/``` you have all of the translation files in csv
   format.

```
ls src/csv/export/
en_GB.csv  
fi_FI.csv  
nl_NL.csv
```

Copy the file ```src/csv/export/en_GB.csv```
to the folder ```src/csv/import``` and rename it after the new language local
in this case nl_BE.csv
```src/csv/export/nl_BE.csv```
The locale codes you can find in
```lib/languageCodes.py```

Open the file and modify the third column, ```Translation (EN_GB)```
as  ```Translation (NL_BE)``` and translate the third column.

*Columns*
```Key```  This column includes the translation key and should not be
modified.
```English```  Here is the source word or sentence, to be translated for
the desired language.
```Translation (NL_BE)``` The column to be translated and filled by the desired language,

```
Key,English,Translation (NL_BE)
pageTitle;Compose Your Letter;Compose Your Letter
previous;Previous;Previous
next;Next;Next
pageTitle;Compose Your Letter;NL Compose Your Letter
previous;Previous;NL Previous
next;Next;NL Next
step1.title;Name and Address;NAW gegevens
step1.properties.name.title;Full Name;Voll1111edige naam
step1.properties.address.title;Address;Adres
step2.title;Optout Out;Optout Out
step2.properties.primaryUse.title;Primary use;Primary use
step2.properties.secondaryUse.title;Secondary use;Secondary use
step3.title;GP Name;Kies je huisarts
step3.properties.gpName.title;Search GP Name;Huisarts naam
step4.title;Choose amount to pay;Hoeveel wil je betalen?
step4.properties.amount.title;Amount (£);
step5.title;Subscribe to Newsletter;Inschrijven voor de nieuwsbrief?
step5.properties.subscribe.title;Subscribe?;Subscribe?
```

3) Run the build command again

```
python build.py
```

4) Now we have a template translated in Belgium Dutch
   ```dist/nl_BE.html```

## Modifying translations

In this case we do the same as in the case "Importing new languages",
but instead of creating a new file we copy an existing file to the folder
```src/csv/import```, modify it and run the build command again.

## Adding translations

1) Build all

```
python build.py
```

2) Copy the file
   ```src/csv/export/en_GB.csv``` to ```src/csv/import/en_GB.csv```
   Make sure that there are no other csv files
   Add a new translation (in the example below we have "newTranslation" on the first row)

```
Key,English,Translation (EN_GB)
newTranslation;new translation;new translation
pageTitle;Compose Your Letter;Compose Your Letter
previous;Previous;Previous
next;Next;Next
```

3) Build again

```
python build.py
```

4) Now in the folder ```src/csv/export```
   We have the cvs files with a new translation as an empty field:
   Example nl_NL.csv

```
Key,English,Translation (NL_NL)
newTranslation;new translation;
pageTitle;Compose Your Letter;NL Compose Your Letter
previous;Previous;NL Previous
next;Next;NL Next
step1.title;Name and Address;NAW gegevens
```

Copy all of the files to the folder

```src/csv/import/```
And fill the empty fields
Example nl_NL.csv

```
Key,English,Translation (NL_NL)
newTranslation;new translation;nieuwe vertaling
pageTitle;Compose Your Letter;NL Compose Your Letter
previous;Previous;NL Previous
next;Next;NL Next
step1.title;Name and Address;NAW gegevens
```

5) After the modifications, build again and
   the translations are updated.

## Folders

### src/languages/

This folder has the translations files in json format
When translating the templates these files are used
to define the translations.

Example: en_GB.json

```
    {
        "pageTitle": "Compose Your Letter",
        "previous": "Previous",
        "next": "Next",
        "step1": {
            "title": "Name and Address",
            "properties": {
                "name": {
                    "title": "Full Name"
                },
            "address": {
                "title": "Address"
                }
            }
        }
    }
  
```

### src/csv/export/

After each build, the existing json files in the folder
```src/languages/``` are exported into this folder in csv format.
These files can be used for the updates of the existing
languages or adding a new languages.

Example:
nl_NL.csv

```
Key,English,Translation (NL_NL)
pageTitle;Compose Your Letter;NiiiL Compose Your Letter
previous;Previous;NL Previous
next;Next;NL Next
step1.title;Name and Address;NAW gegevens
step1.properties.name.title;Full Name;Voll1111edige naam
step1.properties.address.title;Address;Adres
```

### src/csv/import/

In this folder we have the cvs files to be imported to the
json files in the folder ```src/languages/```
The file CSV file structure is the same.

### src/react

Source React Js files to be translated to the folder dist
See how to do this in the section 'React Js'

### dist

The generated html templates are in this folder

### dist/js

Here we have the translations as a a Javascript function,
which can be used in the Javascript code by function _trns
Example:

```
let translationsJson='{"pageTitle": "Compose Your Letter", "previous": "Previous", "next": "Next", "step1.pertires.address.title": "Address"}'; 
let  globalTranslationsObj = JSON.parse(translationsJson); 
function _trns(translation){return(globalTranslationsObj[translation]);}
```



## React Js

The react js  source code can be found in the folder ```src/react```
You edit and modify this folder.

### Intialize and update node_modules
For the first time and updated in the ```node_modules``` you need to run
the ```npm install``` command to install or update.
You do in in the following workflow
1) If needed do updated in the  ```src/react``` for the modules
2) Run the command ```./dockerRunBuildTemplates.sh```
in the root folder ( ```opt_me_out```)
3) Run the build ```npm install``` command in the folder dist
  ```
    cd OptMeOut/dist/
    npm install
  ```

  You can also use the script ```scripts/installNpmModules.sh```


  4) Start the server

  ```
    npm run dev
  ```

  or use  ```scripts/startServer.sh```
    And open

    ```http://localhost:5173/index_en_GB.html ```