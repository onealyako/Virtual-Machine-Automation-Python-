from configparser import ConfigParser
import os
import getpass
from datetime import * 

#Set date/time
now = datetime.now()
times  = now.strftime("%Y-%m-%d:%H:%M:%S")

#Write to file 
fh = open('VMcreation_'+str(times)+".txt",'w')
fh.write("\nDate Stamp: "+str(times))  

# Get admin info of currently logged in user
sysadmin = getpass.getuser()
fh.write("\nSystem Admin Name: "+sysadmin+"\n")

# GCP
def create_gcp_vm():
    # Parse the gcp.conf file
    gcp_file = 'gcp.conf'
    config = ConfigParser()
    config.read(gcp_file)

    # Store the GCP "tags"
    conf_items = (config.sections())

    # Check if there are more than 10 VMs wishing to be created.
    if len(conf_items) > 10:
        print("ERROR: Cannot create more than 10 Virtual Machines.")
    # If not, we can then create VMs
    else: 
        for x in config.sections():
            #Check for 'gcp' tag; else print error message.
            if ((x == "gcp01" ) or (x == "gcp02" ) or (x == "gcp03" ) or (x == "gcp04" ) or (x == "gcp05" ) or (x == "gcp06" ) or (x == "gcp07" ) or (x == "gcp08" ) or (x == "gcp09" ) or (x == "gcp10" )):
            
                # Ensure all required info in gcp.conf 
                if ('name' in config[x]) and ('project' in config[x]) and ('image' in config[x]) and ('imageproject' in config[x]) and ('zone' in config[x]):
                    # Check for unique number in name 
                    if  ("01" in config[x]['name']) or ("02" in config[x]['name']) or ("03" in config[x]['name']) or ("04" in config[x]['name']) or ("05" in config[x]['name']) or ("06" in config[x]['name']) or ("07" in config[x]['name']) or ("08" in config[x]['name']) or ("09" in config[x]['name']) or ("10" in config[x]['name']):
                        
                        # CPU & Memory Size
                        if 'cpu' in config[x]:
                            # Output Memory Info
                            if 'memory' in config[x]:
                            
                                # Perform CPU & Memory  
                                fh.write("\nStatus of the VM\n"+status)
                                fh.write("\nName "+config[x]['name']) 
                                fh.write("\nProject "+config[x]['project'])
                                fh.write("\nPurpose "+config[x]['purpose'])
                                fh.write("\nTeam "+config[x]['team'])
                                fh.write("\nOS "+config[x]['os'])
                                fh.write("\nCPU "+config[x]['cpu'])
                                fh.write("\nMemory "+config[x]['memory'])
                                        
                                print("gcloud compute instances create \""+config[x]['name']+"\" \\")
                                print("--zone "+"\""+config[x]['zone']+"\" \\")
                                print("--image-project "+"\""+config[x]['imageproject']+"\" \\")
                                print("--image "+"\""+config[x]['image']+"\" \\")
                                print("--custom-cpu= "+config[x]['cpu']+" \\")
                                print("--custom-memory= "+config[x]['memory']+" \\")
                                print("--subnet \"default\"")
                                        
                                # Pass commands into OS.SYSTEM(command)
                                status = os.popen("gcloud compute instances create \""+config[x]['name']+"\" \\--zone "+"\""+config[x]['zone']+"\" \\--image-project "+"\""+config[x]['imageproject']+"\" \\--image "+"\""+config[x]['image']+"\" \\--custom-cpu="+config[x]['cpu']+" \\--custom-memory="+config[x]['memory']+" \\--custom-extensions \\--subnet \"default\"").read()
                                print(status)
                                fh.write("\nStatus of the VM\n"+status)
                            
                            # Bare Minimum GCP Conf 
                            else:
                                fh.write("\nName "+config[x]['name']) 
                                fh.write("\nProject "+config[x]['project'])
                                fh.write("\nPurpose "+config[x]['purpose'])
                                fh.write("\nTeam "+config[x]['team'])
                                fh.write("\nOS "+config[x]['os'])
                                
                                print("gcloud compute instances create \""+config[x]['name']+"\" \\")
                                print("--machine-type \"e2-micro\" \\")
                                print("--zone \"northamerica-northeast2-a\" \\")
                                print("--image-project "+"\""+config[x]['imageproject']+"\" \\")
                                print("--image "+"\""+config[x]['image']+"\" \\")
                                print("--subnet \"default\"")
                                
                                # Pass commands into OS.SYSTEM(command)
                                status = os.popen("gcloud compute instances create \""+config[x]['name']+"\" \\--machine-type \"e2-micro\" \\--zone \"northamerica-northeast2-a\" \\--image-project "+"\""+config[x]['imageproject']+"\" \\--image "+"\""+config[x]['image']+"\" \\--subnet \"default\"").read()
                                print(status)
                                fh.write("\nStatus of the VM\n"+status)
                        
                        elif 'diskspace' in config[x]:
                            fh.write("\nName "+config[x]['name']) 
                            fh.write("\nProject "+config[x]['project'])
                            fh.write("\nPurpose "+config[x]['purpose'])
                            fh.write("\nTeam "+config[x]['team'])
                            fh.write("\nOS "+config[x]['os'])
                            fh.write("\nDisk Space "+config[x]['diskspace'])
                                
                            print("gcloud compute instances create \""+config[x]['name']+"\" \\")
                            print("--machine-type \"e2-micro\" \\")
                            print("--zone \"northamerica-northeast2-a\" \\")
                            print("--image-project "+"\""+config[x]['imageproject']+"\" \\")
                            print("--image "+"\""+config[x]['image']+"\" \\")
                            print("--boot-disk-size "+config[x]['diskspace']+ "\\")
                            print("--subnet \"default\"")
                                
                            # Pass commands into OS.SYSTEM(command)
                            status = os.popen("gcloud compute instances create \""+config[x]['name']+"\" \\--machine-type \"e2-micro\" \\--zone \"northamerica-northeast2-a\" \\--image-project "+"\""+config[x]['imageproject']+"\" \\--image "+"\""+config[x]['image']+"\" \\--boot-disk-size "+"\""+config[x]['diskspace']+"\" \\--subnet \"default\"").read()
                            print(status)
                            fh.write("\nStatus of the VM\n"+status)

                        # Bare minimum
                        else:
                            fh.write("\nName "+config[x]['name']) 
                            fh.write("\nProject "+config[x]['project'])
                            fh.write("\nPurpose "+config[x]['purpose'])
                            fh.write("\nTeam "+config[x]['team'])
                            fh.write("\nOS "+config[x]['os'])
                            
                            print("gcloud compute instances create \""+config[x]['name']+"\" \\")
                            print("--machine-type \"e2-micro\" \\")
                            print("--zone \"northamerica-northeast2-a\" \\")
                            print("--image-project "+"\""+config[x]['imageproject']+"\" \\")
                            print("--image "+"\""+config[x]['image']+"\" \\")
                            print("--subnet \"default\"")
                                
                            # Pass commands into OS.SYSTEM(command)
                            status = os.popen("gcloud compute instances create \""+config[x]['name']+"\" \\--machine-type \"e2-micro\" \\--zone \"northamerica-northeast2-a\" \\--image-project "+"\""+config[x]['imageproject']+"\" \\--image "+"\""+config[x]['image']+"\" \\--subnet \"default\"").read()
                            print(status)
                            fh.write("\nStatus of the VM\n"+status)
                    else:
                        print("ERROR: 'name' for tag "+x+" is not allowed. Must be between 01-10. Only can be used once.")

                else:
                    print("ERROR: Failed to create VM with tag "+x+" Ensure you have required info in your .conf file!")
            # Print error message for invalid VM TAG
            else:
                print("\n ERROR: VM Tag "+x+" is not valid.")

# This method will read Azure.conf and create VMs in the .conf file.
def create_azure_vm():

    # Parse the Azure.conf file
    azure_file = 'Azure.conf'
    config_azure = ConfigParser()
    config_azure.read(azure_file)

    # Store Azure tags
    azure_items = (config_azure.sections())

    # Check for max 10 VMs in Azure.conf
    if len(azure_items) > 10:
        print("ERROR: Cannot create more than 10 Virtual Machines.")
    # If not, we can then create VMs
    else: 

        for x in config_azure.sections():
            
            if ((x == "azure01" ) or (x == "azure02" ) or (x == "azure03" ) or (x == "azure04" ) or (x == "azure05" ) or (x == "azure06" ) or (x == "azure07" ) or (x == "azure08" ) or (x == "azure09" ) or (x == "azure10" )):
            
                # Check if Linux or Windows 
                if "linux" in config_azure[x]['os']:
                    
                    if ('name' in config_azure[x]) and ('resource-group' in config_azure[x]) and ('image' in config_azure[x]) and ('location' in config_azure[x]):
                        
                        #Create resource group 
                        os.system("az group create --name "+config_azure[x]['resource-group']+" --location "+config_azure[x]['location']+" --output none")

                        # Check for size in Azure.conf
                        if 'size' in config_azure[x]: 

                            fh.write("\nName "+config_azure[x]['name']) 
                            fh.write("\nPurpose "+config_azure[x]['purpose'])
                            fh.write("\nTeam "+config_azure[x]['team'])
                            fh.write("\nOS "+config_azure[x]['os'])
                            fh.write("\nSize "+config_azure[x]['size'])

                            # Output Azure CLI commands to console
                            print("az vm create \\")
                            print("--resource-group "+config_azure[x]['resource-group']+" \\")
                            print("--location "+config_azure[x]['location']+" \\")
                            print("--name "+config_azure[x]['name']+" \\")
                            print("--image "+config_azure[x]['image']+" \\")
                            print("--admin-username "+config_azure[x]['admin-username']+" \\")
                            print("--admin-password "+config_azure[x]['admin-password']+" \\")   
                            print("--size "+config_azure[x]['size']+" \\")
                            print("--generate-ssh-keys \\")
                            print("--verbose")

                            # Pass commands into OS.SYSTEM(command)
                            os.system("az vm create \\--resource-group "+config_azure[x]['resource-group']+" \\--location "+config_azure[x]['location']+" \\--name "+config_azure[x]['name']+" \\--image "+config_azure[x]['image']+" \\--admin-username "+config_azure[x]['admin-username']+" \\--admin-password "+config_azure[x]['admin-password']+" \\--size "+config_azure[x]['size']+" \\--generate-ssh-keys \\--verbose --out table")
                            
                            # Write status to text file
                            status = os.popen("az vm get-instance-view --name "+config_azure[x]['name']+ " --resource-group "+config_azure[x]['resource-group']+ " --output table").read()
                            fh.write("\nStatus of the VM\n"+status)
                        
                        # If disk size is specified in azure.conf
                        elif 'diskspace' in config_azure[x]:
                            # Check if port also specified with diskspace
                            if 'port' in config_azure[x]: 
                                fh.write("\nName "+config_azure[x]['name']) 
                                fh.write("\nPurpose "+config_azure[x]['purpose'])
                                fh.write("\nTeam "+config_azure[x]['team'])
                                fh.write("\nOS "+config_azure[x]['os'])
                                fh.write("\nPort "+config_azure[x]['port'])
                                fh.write("\nDisk Space "+config_azure[x]['diskspace'])
                                
                                # Output Azure CLI commands to console
                                print("az vm create \\")
                                print("--resource-group "+config_azure[x]['resource-group']+" \\")
                                print("--location "+config_azure[x]['location']+" \\")
                                print("--name "+config_azure[x]['name']+" \\")
                                print("--image "+config_azure[x]['image']+" \\")
                                print("--admin-username "+config_azure[x]['admin-username']+" \\")
                                print("--admin-password "+config_azure[x]['admin-password']+" \\")  
                                print("--os-disk-size-gb "+config_azure[x]['diskspace']+" \\")  
                                print("--generate-ssh-keys \\")
                                print("--verbose")
                                print("az vm open-port --port "+config_azure[x]['port']+" -g "+config_azure[x]['resource-group']+" -n "+config_azure[x]['name'])

                                # Pass commands into OS.SYSTEM(command)
                                os.system("az vm create \\--resource-group "+config_azure[x]['resource-group']+" \\--location "+config_azure[x]['location']+" \\--name "+config_azure[x]['name']+" \\--image "+config_azure[x]['image']+" \\--admin-username "+config_azure[x]['admin-username']+" \\--admin-password "+config_azure[x]['admin-password']+" \\--os-disk-size-gb "+config_azure[x]['diskspace']+" \\--generate-ssh-keys \\--verbose --out table")
                                os.system("az vm open-port --port "+config_azure[x]['port']+" -g "+config_azure[x]['resource-group']+" -n "+config_azure[x]['name']+" --output none")

                                # Write status to text file
                                status = os.popen("az vm get-instance-view --name "+config_azure[x]['name']+ " --resource-group "+config_azure[x]['resource-group']+ " --output table").read()
                                fh.write("\nStatus of the VM\n"+status)
                            else:

                                fh.write("\nName "+config_azure[x]['name']) 
                                fh.write("\nPurpose "+config_azure[x]['purpose'])
                                fh.write("\nTeam "+config_azure[x]['team'])
                                fh.write("\nOS "+config_azure[x]['os'])
                                fh.write("\nDisk Space "+config_azure[x]['diskspace'])
                                
                                # Output Azure CLI commands to console
                                print("az vm create \\")
                                print("--resource-group "+config_azure[x]['resource-group']+" \\")
                                print("--location "+config_azure[x]['location']+" \\")
                                print("--name "+config_azure[x]['name']+" \\")
                                print("--image "+config_azure[x]['image']+" \\")
                                print("--admin-username "+config_azure[x]['admin-username']+" \\")
                                print("--admin-password "+config_azure[x]['admin-password']+" \\")  
                                print("--os-disk-size-gb "+config_azure[x]['diskspace']+" \\")  
                                print("--generate-ssh-keys \\")
                                print("--verbose")

                                # Pass commands into OS.SYSTEM(command)
                                os.system("az vm create \\--resource-group "+config_azure[x]['resource-group']+" \\--location "+config_azure[x]['location']+" \\--name "+config_azure[x]['name']+" \\--image "+config_azure[x]['image']+" \\--admin-username "+config_azure[x]['admin-username']+" \\--admin-password "+config_azure[x]['admin-password']+" \\--os-disk-size-gb "+config_azure[x]['diskspace']+" \\--generate-ssh-keys \\--verbose --out table")

                                # Write status to text file
                                status = os.popen("az vm get-instance-view --name "+config_azure[x]['name']+ " --resource-group "+config_azure[x]['resource-group']+ " --output table").read()
                                fh.write("\nStatus of the VM\n"+status)

                        # If port is specified in azure.conf
                        elif 'port' in config_azure[x]: 
                            fh.write("\nName "+config_azure[x]['name']) 
                            fh.write("\nPurpose "+config_azure[x]['purpose'])
                            fh.write("\nTeam "+config_azure[x]['team'])
                            fh.write("\nOS "+config_azure[x]['os'])
                            fh.write("\nPort "+config_azure[x]['port'])
                            

                            # Output Azure CLI commands to console
                            print("az vm create \\")
                            print("--resource-group "+config_azure[x]['resource-group']+" \\")
                            print("--location "+config_azure[x]['location']+" \\")
                            print("--name "+config_azure[x]['name']+" \\")
                            print("--image "+config_azure[x]['image']+" \\")
                            print("--admin-username "+config_azure[x]['admin-username']+" \\")
                            print("--admin-password "+config_azure[x]['admin-password']+" \\")  
                            print("--generate-ssh-keys \\")
                            print("--verbose")
                            print("az vm open-port --port "+config_azure[x]['port']+" -g "+config_azure[x]['resource-group']+" -n "+config_azure[x]['name'])

                            # Pass commands into OS.SYSTEM(command)
                            os.system("az vm create \\--resource-group "+config_azure[x]['resource-group']+" \\--location "+config_azure[x]['location']+" \\--name "+config_azure[x]['name']+" \\--image "+config_azure[x]['image']+" \\--admin-username "+config_azure[x]['admin-username']+" \\--admin-password "+config_azure[x]['admin-password']+" \\--generate-ssh-keys \\--verbose --out table")
                            os.system("az vm open-port --port "+config_azure[x]['port']+" -g "+config_azure[x]['resource-group']+" -n "+config_azure[x]['name']+" --output none")

                            # Write status to text file
                            status = os.popen("az vm get-instance-view --name "+config_azure[x]['name']+ " --resource-group "+config_azure[x]['resource-group']+ " --output table").read()
                            fh.write("\nStatus of the VM\n"+status)

                        # Do standard/base requirements as per assignment specs
                        else:
                            fh.write("\nName "+config_azure[x]['name']) 
                            fh.write("\nPurpose "+config_azure[x]['purpose'])
                            fh.write("\nTeam "+config_azure[x]['team'])
                            fh.write("\nOS "+config_azure[x]['os'])
                
                            print("az vm create \\")
                            print("--resource-group "+config_azure[x]['resource-group']+" \\")
                            print("--location "+config_azure[x]['location']+" \\")
                            print("--name "+config_azure[x]['name']+" \\")
                            print("--image "+config_azure[x]['image']+" \\")
                            print("--admin-username "+config_azure[x]['admin-username']+" \\")
                            print("--generate-ssh-keys \\")
                            print("--verbose")

                            # Pass commands into OS.SYSTEM(command)
                            os.system("az vm create \\--resource-group "+config_azure[x]['resource-group']+" \\--location "+config_azure[x]['location']+" \\--name "+config_azure[x]['name']+" \\--image "+config_azure[x]['image']+" \\--admin-username "+config_azure[x]['admin-username']+" \\--admin-password "+config_azure[x]['admin-password']+" \\--generate-ssh-keys \\--verbose --out table")
                            
                            # Write status to text file
                            status = os.popen("az vm get-instance-view --name "+config_azure[x]['name']+ " --resource-group "+config_azure[x]['resource-group']+ " --output table").read()
                            fh.write("\nStatus of the VM\n"+status)
                                            
                    else:
                        print("ERROR: Failed to create VM with tag "+x+" Ensure you have required flags in your .conf file!")
                
                # Perform Windows Azure VM spec requirements
                elif "windows" in config_azure[x]['os']:

                    #Create resource group 
                    os.system("az group create --name "+config_azure[x]['resource-group']+" --location "+config_azure[x]['location']+" --output none")
                    
                    if ('name' in config_azure[x]) and ('resource-group' in config_azure[x]) and ('image' in config_azure[x]) and ('location' in config_azure[x]):
                        # Check for size in Azure.conf
                        if 'size' in config_azure[x]: 
                            
                            fh.write("\nName "+config_azure[x]['name']) 
                            fh.write("\nPurpose "+config_azure[x]['purpose'])
                            fh.write("\nTeam "+config_azure[x]['team'])
                            fh.write("\nOS "+config_azure[x]['os'])
                            fh.write("\nSize "+config_azure[x]['size'])    
                                               
                            # Output Azure CLI commands to console
                            print("az vm create \\")
                            print("--resource-group "+config_azure[x]['resource-group']+" \\")
                            print("--location "+config_azure[x]['location']+" \\")
                            print("--name "+config_azure[x]['name']+" \\")
                            print("--image "+config_azure[x]['image']+" \\")
                            print("--admin-username "+config_azure[x]['admin-username']+" \\")
                            print("--admin-password "+config_azure[x]['admin-password']+" \\")  
                            print("--size "+config_azure[x]['size']+" \\")
                            print("--generate-ssh-keys \\")
                            print("--verbose")

                            # Pass commands into OS.SYSTEM(command)
                            os.system("az vm create \\--resource-group "+config_azure[x]['resource-group']+" \\--location "+config_azure[x]['location']+" \\--name "+config_azure[x]['name']+" \\--image "+config_azure[x]['image']+" \\--admin-username "+config_azure[x]['admin-username']+" \\--admin-password "+config_azure[x]['admin-password']+" \\--size "+config_azure[x]['size']+" \\--generate-ssh-keys \\--verbose --out table")

                            # Write status to text file
                            status = os.popen("az vm get-instance-view --name "+config_azure[x]['name']+ " --resource-group "+config_azure[x]['resource-group']+ " --output table").read()
                            fh.write("\nStatus of the VM\n"+status)

                        # If disk size is specified in azure.conf
                        elif 'diskspace' in config_azure[x]:
                            # Check if port also specified with diskspace
                            if 'port' in config_azure[x]: 
                                fh.write("\nName "+config_azure[x]['name']) 
                                fh.write("\nPurpose "+config_azure[x]['purpose'])
                                fh.write("\nTeam "+config_azure[x]['team'])
                                fh.write("\nOS "+config_azure[x]['os'])
                                fh.write("\nPort "+config_azure[x]['port'])
                                fh.write("\nDisk Space "+config_azure[x]['diskspace'])
                                
                                # Output Azure CLI commands to console
                                print("az vm create \\")
                                print("--resource-group "+config_azure[x]['resource-group']+" \\")
                                print("--location "+config_azure[x]['location']+" \\")
                                print("--name "+config_azure[x]['name']+" \\")
                                print("--image "+config_azure[x]['image']+" \\")
                                print("--admin-username "+config_azure[x]['admin-username']+" \\")
                                print("--admin-password "+config_azure[x]['admin-password']+" \\")  
                                print("--os-disk-size-gb "+config_azure[x]['diskspace']+" \\")  
                                print("--generate-ssh-keys \\")
                                print("--verbose")
                                print("az vm open-port --port "+config_azure[x]['port']+" -g "+config_azure[x]['resource-group']+" -n "+config_azure[x]['name'])

                                # Pass commands into OS.SYSTEM(command)
                                os.system("az vm create \\--resource-group "+config_azure[x]['resource-group']+" \\--location "+config_azure[x]['location']+" \\--name "+config_azure[x]['name']+" \\--image "+config_azure[x]['image']+" \\--admin-username "+config_azure[x]['admin-username']+" \\--admin-password "+config_azure[x]['admin-password']+" \\--os-disk-size-gb "+config_azure[x]['diskspace']+" \\--generate-ssh-keys \\--verbose --out table")
                                os.system("az vm open-port --port "+config_azure[x]['port']+" -g "+config_azure[x]['resource-group']+" -n "+config_azure[x]['name']+" --output none")

                                # Write status to text file
                                status = os.popen("az vm get-instance-view --name "+config_azure[x]['name']+ " --resource-group "+config_azure[x]['resource-group']+ " --output table").read()
                                fh.write("\nStatus of the VM\n"+status)
                            else:

                                fh.write("\nName "+config_azure[x]['name']) 
                                fh.write("\nPurpose "+config_azure[x]['purpose'])
                                fh.write("\nTeam "+config_azure[x]['team'])
                                fh.write("\nOS "+config_azure[x]['os'])
                                fh.write("\nDisk Space "+config_azure[x]['diskspace'])
                                
                                # Output Azure CLI commands to console
                                print("az vm create \\")
                                print("--resource-group "+config_azure[x]['resource-group']+" \\")
                                print("--location "+config_azure[x]['location']+" \\")
                                print("--name "+config_azure[x]['name']+" \\")
                                print("--image "+config_azure[x]['image']+" \\")
                                print("--admin-username "+config_azure[x]['admin-username']+" \\")
                                print("--admin-password "+config_azure[x]['admin-password']+" \\")  
                                print("--os-disk-size-gb "+config_azure[x]['diskspace']+" \\")  
                                print("--generate-ssh-keys \\")
                                print("--verbose")

                                # Pass commands into OS.SYSTEM(command)
                                os.system("az vm create \\--resource-group "+config_azure[x]['resource-group']+" \\--location "+config_azure[x]['location']+" \\--name "+config_azure[x]['name']+" \\--image "+config_azure[x]['image']+" \\--admin-username "+config_azure[x]['admin-username']+" \\--admin-password "+config_azure[x]['admin-password']+" \\--os-disk-size-gb "+config_azure[x]['diskspace']+" \\--generate-ssh-keys \\--verbose --out table")

                                # Write status to text file
                                status = os.popen("az vm get-instance-view --name "+config_azure[x]['name']+ " --resource-group "+config_azure[x]['resource-group']+ " --output table").read()
                                fh.write("\nStatus of the VM\n"+status)

                        elif 'port' in config_azure[x]:
                            fh.write("\nName "+config_azure[x]['name']) 
                            fh.write("\nPurpose "+config_azure[x]['purpose'])
                            fh.write("\nTeam "+config_azure[x]['team'])
                            fh.write("\nOS "+config_azure[x]['os'])
                            fh.write("\nPort "+config_azure[x]['port'])

                             # Output Azure CLI commands to console
                            print("az vm create \\")
                            print("--resource-group "+config_azure[x]['resource-group']+" \\")
                            print("--location "+config_azure[x]['location']+" \\")
                            print("--name "+config_azure[x]['name']+" \\")
                            print("--image "+config_azure[x]['image']+" \\")
                            print("--admin-username "+config_azure[x]['admin-username']+" \\")
                            print("--admin-password "+config_azure[x]['admin-password']+" \\")  
                            print("--generate-ssh-keys \\")
                            print("--verbose")

                            print("az vm open-port --port "+config_azure[x]['port']+" -g "+config_azure[x]['resource-group']+" -n "+config_azure[x]['name'])
                            
                            # Pass commands into OS.SYSTEM(command)
                            os.system("az vm create \\--resource-group "+config_azure[x]['resource-group']+" \\--location "+config_azure[x]['location']+" \\--name "+config_azure[x]['name']+" \\--image "+config_azure[x]['image']+" \\--admin-username "+config_azure[x]['admin-username']+" \\--admin-password "+config_azure[x]['admin-password']+" \\--generate-ssh-keys \\--verbose --out table")
                            os.system("az vm open-port --port "+config_azure[x]['port']+" -g "+config_azure[x]['resource-group']+" -n "+config_azure[x]['name']+" --output none")

                        # Do standard/base requirements as per assignment specs
                        else:
                            fh.write("\nName "+config_azure[x]['name']) 
                            fh.write("\nPurpose "+config_azure[x]['purpose'])
                            fh.write("\nTeam "+config_azure[x]['team'])
                            fh.write("\nOS "+config_azure[x]['os'])                            

                            print("az vm create \\")
                            print("--resource-group "+config_azure[x]['resource-group']+" \\")
                            print("--location "+config_azure[x]['location']+" \\")
                            print("--name "+config_azure[x]['name']+" \\")
                            print("--image "+config_azure[x]['image']+" \\")
                            print("--admin-username "+config_azure[x]['admin-username']+" \\")
                            print("--admin-password "+config_azure[x]['admin-password']+" \\")    
                            print("--generate-ssh-keys \\")
                            print("--verbose")

                            # Pass commands into OS.SYSTEM(command)
                            os.system("az vm create \\--resource-group "+config_azure[x]['resource-group']+" \\--location "+config_azure[x]['location']+" \\--name "+config_azure[x]['name']+" \\--image "+config_azure[x]['image']+" \\--admin-username "+config_azure[x]['admin-username']+" \\--admin-password "+config_azure[x]['admin-password']+" \\--generate-ssh-keys \\--verbose --out table")
                            # Write status to text file
                            status = os.popen("az vm get-instance-view --name "+config_azure[x]['name']+ " --resource-group "+config_azure[x]['resource-group']+ " --output table").read()
                            fh.write("\nStatus of the VM\n"+status)
                        
                    else:
                        print("ERROR: Failed to create VM with tag "+x+" Ensure you have required flags in your .conf file!")
                # If OS is not Windows or Linux, print error to user.
                else:
                    print("ERROR: OS for tag "+x+" not correct. Must be Linux or Windows OS!")
            # Print error message for invalid VM TAG
            else:
                print("\n ERROR: VM Tag "+x+" is not valid.\n")


# Run program to create Azure & GCP VMs
create_azure_vm()
create_gcp_vm()