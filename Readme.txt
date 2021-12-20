# O'Neal Yako
# CLOUD COMPUTING

--How to Run Program--

**In Mac terminal, I used below and it ran without any errors**: 
     python3 automate.py

** TO EXIT PROGRAM: User must do a keyboard interrupt in terminal.

My Quick Assumptions/General Comments:
--------------------------------------
-- I am assuming that the azure.conf gcp.conf will be in the same location as my program.
-- My program will not prompt user for directory input & can only read the specific .conf 
   files (azure.conf, gcp.conf)
-- I am assuming that you will already be authenticated and have a project open for GCP.
-- I am assuming you will already be logged in & authenticated for Azure as well.
-- In the text file that is generated, the System Admin should be the username of the device owner. 
   Example: My Macbook username/account login is onealyako. That is displayed for system admin in the text.

** I have added the ability to specify port, diskspace, size, memory/cpu in Azure & GCP. 

GCP VM General Comments: 
------------------------
-- Due to Windows VMs not being included in free trial, I have used different Linux VMs. However, if you specify
   Windows VMs, i believe it should work.

-- You can create VMs with the basic gcp.conf as per assignment specs. 
-- You can also create VMs with 'cpu' and 'memory' specified. 
-- You can also create VMs with diskspace specified. 
   NOTE: You cannot specify diskspace, cpu, memory at the same time. Diskspace must be specfied separately. 
    
    ** CPU & Memory in GCP VM: **
        - You are able to specify CPU size and Memory. 
        - The two must be specified together or 
           else GCP will complain. You CANNOT specify only CPU or only Memory.
        - The zone specified may/may not work depending on whether the zone has enough resources
          available to fulfill the request. Different zone may be needed. For my gcp.conf, 
          I get an error with 'northamerica-northeast2-a', however it successfully creates in 'us-west4-a'
        - If you want to test for CPU and memory, make sure you write it the way its been 
          written in the included GCP.conf file. There cannot be any 
          extra tags otherwise my program will not read it.

        SAMPLE specification of CPU & Memory size in gcp.conf:
                            [gcp02]
                            name = linuxserver02
                            project = Web Pres Canada
                            team = Torono
                            purpose = webservers
                            os = linux 
                            image = rhel-8-1-sap-v20211105 
                            imageproject = rhel-sap-cloud
                            zone = us-west4-a
                    -->     cpu = 2
                    -->     memory = 2048MB

   ** Disk Space Specification in GCP VM **
         - You can specify diskspace. Minimum is 10GB. 
         - In my gcp.conf, i have a sample of how it looks.
         
         SAMPLE of diskspace specification in gcp.conf:
                     [gcp01]
                     name = linuxserver01
                     project = Web Life New York
                     team = Torono
                     purpose = webserv
                     os = linux 
                     image = debian-10-buster-v20210916
                     imageproject = debian-cloud
                     zone = northamerica-northeast2-a
               -->   diskspace = 10GB

Azure VM General Comments: 
-------------------------
-- Since 'Project' is not included in any part of Azure.conf, i have not allowed it to be specified in the text file created.
-- admin-password required for Linux & Windows VMs. You can specify your password
   properly in the azure.conf. This is made to help you while grading so you do not 
   have to manually input password for each VM. 
-- You can create VMs with the basic setup azure.conf as per assignment specs
-- You can also create VMs with 'size' and 'port' specified (individually). 
   NOTE: You cannot specify port & size together. They must be specified individually in the azure.conf
-- You can also specify disk size (GB) 
   NOTE: This extra specification can be specified with port or by individually in the azure.conf

    ** Size in Azure VM **
        -- You can specify size like sample below:
        -- NOTE: The admin-password should also be specified to speed-up VM creation process
                 in the event that a password is required, as my program should be able to 
                 handle admin-password in the conf.

        SAMPLE 'size' specification in azure.conf 
                                [azure01]
                                purpose = webserver
                                os = linux
                                name = linuxServer01 
                                resource-group = vms 
                                team = Vancouver
                                image = Debian 
                                location = canadacentral
                                admin-username = oyako
                        -->     admin-password = PoliceacademyU18!
                        -->     size = Standard_B1ls

    ** Port Specification in Azure VM **
        -- Port can be specified: '80' or '400' or '80,400'
        
        SAMPLE of 'port' specification in azure.conf:
                    [azure02]
                    purpose = webserver
                    os = linux
                    name = linuxServer02 
                    resource-group = demoResoruceGroup
                    team = Toronto
                    image = Win2012Datacenter  
                    location = canadacentral
                    admin-username = oyako
                    admin-password = PoliceacademyU18!
            -->     port = 80,400   
            
            Can also specify separately:   port = 80
                                           port = 400

      ** Disk Size (GB) in Azure VM **
         -- Can only enter a numeric digit ('30')
         -- Can be specified with port in the azure.conf
         -- Minimum GB allowed is 30GB. Follow Azure Error given if you specify too little/too much.

         SAMPLE of disk size specification in azure.conf:
                    [azure02]
                    purpose = webserver
                    os = linux
                    name = linuxServer02 
                    resource-group = demoResoruceGroup
                    team = Toronto
                    image = Win2012Datacenter  
                    location = canadacentral
                    admin-username = oyako
                    admin-password = PoliceacademyU18!
            -->     diskspace = 30

         SAMPLE of disk size & port specification in azure.conf:
                     [azure02]
                     purpose = webserver
                     os = linux
                     name = linuxServer02 
                     resource-group = demoResoruceGroup
                     team = Toronto
                     image = Win2012Datacenter  
                     location = canadacentral
                     admin-username = azureuser
                     admin-password = PoliceacademyU18!
               -->   diskspace = 127
               -->   port = 80,400

        
