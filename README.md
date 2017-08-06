# SyncS

How to Use ?

1) create a configuration file using JSON structure and save in config/ folder.

2) Using the structure like this:
{
    "sites": [
        {
            "website": "site exemplo", 
            "from": "/var/www/teste/", 
            "to": "/var/www/teste.backup/"
        }
    ]
}

3) To call the script use the cli like this

python syncs.py --type daily

