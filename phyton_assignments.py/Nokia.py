

print( "LIST OF MENU FUNCTION enter ctrl +  Z to quit ")
print ("1-> Phone Book \n"  "2-> Message \n"  "3-> chat \n"  "4-> Call register \n"  "5-> Tone \n"  "6-> Setting \n"  "7-> Call Divert \n"  "8-> Games \n"  "9-> Calculator \n"  "10-> Reminders \n"  "11-> Clock \n"  "12-> Profile \n"  "13 -> Sim Services \n"  "Select options : ")
print( "\n\n")
phoneMenu = int(input("enter an option here"))
if phoneMenu==1:
                print ("PHONE BOOK \n" + "1-> search \n" + "2 -> Service Nos \n" + "3 -> Add Name \n" + "4 -> Erase\n" + "5 -> Edit \n" + "6 -> Assign tone \n" + "7 -> Send b'card \n" + "8 -> options \n 1. Type of view \n 2. Memory status \n" + "9 -> Speed dials \n" + "10 -> Voice tags \n" + "select options ")
                phoneBook = int(input("enter an option"))
                if phoneBook==1:
                    print ("welcome to search")
                elif phoneBook==2:
                    print ("Welcome to service Nos")
                elif phoneBook==3:
                    print ("welcome to add name ")
                elif phoneBook==4:
                    print ("Add Name")
                elif phoneBook==5:
                    print  ("Erase")
                elif phoneBook==6:
                    print ("Edit")
                elif phoneBook==7:
                    print ("Assign Tone")
                elif phoneBook==8:
                     print( "OPTIONS\n" "1 -> Type of view\n" "2 -> Memory status\n")
                     options = int(input("enter an option "))
                     if options==1:
                        print ("Welcome to Type of view")
                     elif options==2:
                        print ("Welcome to Memory satus")
                     else:
                        print ("Wrong command entered ")
                elif phoneBook==9:
                    print ("Welcome to Speed dials")
                elif phoneBook==10:
                    print ("Welcome to Voice tags")
                else:
                    print ("wrong command entered")
elif phoneMenu==2:
                print( "messages\n  ->write messages\n  ->inbox\n ->outbox\n ->picture messages\n ->Templates\n  ->Smileys\n ->Messages settings\n  1.set\n  1.messages centre number\n    2.messages sent as\n    3.messages validity\n 2.Common\n     1.delivery reports\n    2.reply via same centre\n    3.character support\n ->info services\n ->voice mailbox number\n -> service command editor\n  select an action!/n" )
                action = int(input("enter an action"))
                if action==1:
                    print ("write messages")
                elif action==2:
                    print ("inbox")
                elif action==3:
                    print ("outbox")
                elif action==4:
                    print ("picture messages")
                elif action==5:
                    print ("Templates")
                elif action==6:
                    print ("Smileys")
                elif action==7:
                    System.out.printf("%S%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n", "messages settings", " ->set1 ", " 1.message centre number", "2.messages sent as ", "3.messages validity", " ->common", " 1.delivery reports", " 3.character support")
                    if Msettings==1:
                        print ("set 1")
                    elif Msettings==2:
                        print ("Common")
                    else:
                        print ("Wrong command entered ")
                    print ("choose an option from above")
                    if SetOpp / 1==1:
                        print ("messages centre number")
                        print ("messages sent as")
                        print ("message validity")
                    elif SetOpp / 1==2:
                        print ("delivery reports")
                        print ("reply via same centre")
                        print ("character support")
                    else:
                        print ("Wrong command entered ")
                elif action==8:
                    print ("info services")
                elif action==9:
                    print ("voice mail number")
                elif action==10:
                    print ("service command editor")
elif phoneMenu==3:
                 print ("welcome to chat")
elif phoneMenu==4:
                System.out.printf("%s%n %s%n %s%n %s%n %s%n %s%n  %s%n %s%n %s%n %s%n %s%n %s%n %s%n %s%n  ", "call Register", "1.Missed call", " 2.Recieved call", "3.Dailed numbers", "4.Erase recent call lists", "5.clear timers", "6.show call costs", "1.last call cost", "  2.All calls' cost", "3.clear counter", "7.call cost settings", "1.call cost limit", "2.Show costs in", "8.prepaid credit")
                print ("select an option")
                if fourPtion==1:
                    print ("Missed calls")
                elif fourPtion==2:
                    print ("Recieved calls")
                elif fourPtion==3:
                    print ("Dailed calls")
                elif fourPtion==4:
                    print ("Erase recent call lists")
                elif fourPtion==5:
                    System.out.printf("%s%n %s%n %s%n %s%n %s%n %s%n", "show call duration", " 1.last call duration", "2. All calls' cost", "3. Recieved calls's duration ", "Dialed calls' duration ", "clear timers")
                    print ("select an option here")
                    if hereOptions==1:
                        print ("last call durations ")
                    elif hereOptions==2:
                        print ("All calls' costs")
                    elif hereOptions==3:
                        print ("Recieved calls' duration")
                    elif hereOptions==4:
                        print ("Dailed calls' duration")
                    elif hereOptions==5:
                        print ("Clear timers ")
                    else:
                        print ("Wrong command entered ")
                elif fourPtion==6:
                    System.out.printf("%s%n %s%n %s%n %s%n ", "show call costs", "1. last call cost ", "2. all calls' cost ", "clear counters")
                    print ("select an option here")
                    if hereCptions==1:
                        print ("check your last call cost")
                    elif hereCptions==2:
                        print ("check all call cost")
                    elif hereCptions==3:
                        print ("clear all counters")
                    else:
                        print ("Wrong command entered ")
                elif fourPtion==7:
                    System.out.printf("%S%n %s%n %s%n", "call cost settings", "1.calls' costs limit", "2.show costs in")
                    print( "select an option here")
                    if sevenOpt==1:
                        print ("your call cost limit")
                    elif sevenOpt==2:
                        print ("show your costs in")
                    else:
                        print ("Wrong command entered ")
                elif fourPtion==8:
                    print ("PREPAID CREDIT")
elif phoneMenu==5:
                System.out.printf("%S%n%n %s%n %s%n %s%n %s%n %s%n %s%n %s%n %s%n %s%n", "-->tones", "1.ringing tone", "2.ringing volume", "3.incoming call alert", "4.composer", "5.Message alert tone", "6.keypad tones", "7.warning and games tones", "8.vibrating alert", "9.screen saver")
                print ("select an option here")
                if fifthOpt==1:
                    print ("Customize your ringing tone")
                elif fifthOpt==2:
                    print ("Adjust your ringing volume")
                elif fifthOpt==3:
                    print ("Incoming call alert")
                elif fifthOpt==4:
                    print ("composer")
                elif fifthOpt==5:
                    print ("message alert tone")
                elif fifthOpt==6:
                    print ("customize your keypad tones")
                elif fifthOpt==7:
                    print ("warning and game tones")
                elif fifthOpt==8:
                    print ("vibrating alert")
                elif fifthOpt==9:
                    print ("Screen saver")
                else:
                    print ("Wrong command entered ")
elif phoneMenu==6:
                System.out.printf("%S%n%n %s%n %s%n %s%n %s%n", "-->Settings", "1.call settings", "2.phone settings", "3.Security settings", "4.restore  ")
                print ("select an option here")
                if sixthOpt / 1==1:
                    System.out.printf("%S%n%n %s%n %s%n %s%n %s%n %s%n %s%n", "-->call Settings", "1.Automatic redial", "2.speed dialing", "3.call waiting options", "4.own number sending", "5.phone line in use ", "6.Automatic answer ")
                    print ("select an option here")
                    if Case1Of4==1:
                        print ("Automatic redial")
                    elif Case1Of4==2:
                        print ("speed dialing")
                    elif Case1Of4==3:
                        print ("call waiting options")
                    elif Case1Of4==4:
                        print ("own number sending")
                    elif Case1Of4==5:
                        print ("phone line in use ")
                    elif Case1Of4==6:
                        print ("Automatic answer ")
                    else:
                        print ("Wrong command entered ")
                elif sixthOpt / 1==2:
                    System.out.printf("%S%n%n %s%n %s%n %s%n %s%n %s%n %s%n", "-->phone Settings", "1.language", "2.cell info display", "3.welcome note", "4.network selection", "5.Lights ", "6.Confirm SIM service actions")
                    print ("select an option here")
                    if Case2Of4==1:
                        print ("language")
                    elif Case2Of4==2:
                        print ("cell info display")
                    elif Case2Of4==3:
                        print ("welcome note")
                    elif Case2Of4==4:
                        print ("network selection")
                    elif Case2Of4==5:
                        print ("Lights")
                    elif Case2Of4==6:
                        print ("Confirm SIM service actions ")
                    else:
                        print ("Wrong command entered ")
                elif sixthOpt / 1==3:
                    System.out.printf("%S%n%n %s%n %s%n %s%n %s%n %s%n %s%n", "-->security Settings", "1.PIN code request", "2.Call barring service", "3.Fixed dialling", "4.closed user group", "5.phone security ", "6.change access codes")
                    print ("select an option here")
                    if Case3Of4==1:
                        print (".PIN code request")
                    elif Case3Of4==2:
                        print ("Call barring service")
                    elif Case3Of4==3:
                        print ("Fixed dialling")
                    elif Case3Of4==4:
                        print ("closed user group")
                    elif Case3Of4==5:
                        print ("phone security ")
                    elif Case3Of4==6:
                        print ("change access codes")
                    else:
                        print ("Wrong command entered ")
                elif sixthOpt / 1==4:
                    print ("Restore factory settings !!! ")
elif phoneMenu==7:
                print (" call divert ")
elif phoneMenu==8:
                print (" GAME ")
elif phoneMenu==9:
                print ("CALCULATOR")
elif phoneMenu==10:
                print (" REMINDERS ")
elif phoneMenu==11:
                printf( "-->CLOCK " "1.Alarm clock" "2.Clock settings" "3.Date Settings" "4.Stopwatch" "5.Countdown timer " "6.Auto update date and time")
               
                C11 = int(input("enter an option"))
                if C11==1:
                    print ("Alarm clock")
                elif C11==2:
                    print ("Clock settings")
                elif C11==3:
                    print ("Date Settings")
                elif C11==4:
                    print ("Stopwatch")
                elif C11==5:
                    print ("Countdown timer ")
                elif C11==6:
                    print ("Auto update date and time")
                else:
                    print ("Wrong command entered ")
elif phoneMenu==12:
                print (" Profiles ")
elif phoneMenu==13:
                print ("SIM services")
else:
                   print ("Wrong command entered ")
  
    