
[IRDB](https://github.com/Lucaslhm/Flipper-IRDB) is a great resource with plenty of files to control your electronics.


The easiest way to get these files onto your flipper is to:

1. Download the IRDB repo as a [zip file](https://github.com/logickworkshop/Flipper-IRDB/archive/refs/heads/main.zip) and extract it (on your computer).
2. Un-mount the micro SD card properly from your flipper, and insert it into your computer. 
3. (OPTIONAL BUT RECOMMENDED) Clean up the IRDB folder using the provided scripts to remove unnecessary files.
4. (OPTIONAL) You can swap out the flipper universal remotes with the universal remotes from the IRDB repo. Please follow the instructions in the IRDB README for that.
5. Then, navigate to the `ir/IRDB` folder on your flipper's micro SD card, and copy the contents of the `IRDB` folder you extracted from the zip file to your flipper's `ir/IRDB` folder.
 

### Step 3: Cleaning up the IRDB folder

1. There are pictures (and other file types) that show up in the DB which will increase the file size and are not useful for the flipper. 

2. There are many IR files that you will never use but still take up space and make it harder to find the files you do want.

Scripts to help solve the 1st problem:

- filetypes.py: This script will scan your IRDB folder and report the file types it finds, helping you understand what files are present.

- cleaner.py: This script will remove unnecessary files from your IRDB folder, leaving only the IR files that are relevant for your flipper. The overall folder structure will be preserved. CAUTION: This script will delete files in the directory you provide, this is a destructive operation. Only provide the script with the path to the IRDB folder you want to clean up.

You can either ignore the 2nd problem (and copy everything), or curate the IR files you want to keep manually. 

### Other Notes

IRDB is a community-driven project, so the quality and completeness of the files may vary. If you find missing or incorrect files, consider contributing back to the IRDB project. The repository is open-source, and contributions are welcome. It is worthwhile checking back on the IRDB project periodically for updates, as new files are added and existing ones are improved.