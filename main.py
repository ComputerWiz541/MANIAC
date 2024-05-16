import nextcord
from nextcord.ext import commands
from nextcord.ext import tasks


import random

from datetime import datetime
import os

bot = commands.Bot()
events_file = 'events.txt'
allowed_user_id = 1084262700080713768 #Me
#allowed_user_id = 1131695099756150844 #Alt
log_file = 'logs.txt'




"""

@tasks.loop(seconds=60)  # Adjust the interval as needed
async def check_event_dates():
    current_time = datetime.now()
    with open(events_file, 'r') as file:
        for line in file:
            event_name, event_date_str = line.strip().split(',')
            event_date = datetime.strptime(event_date_str, '%Y-%m-%d %H:%M')
            if event_date <= current_time:
                guild = bot.get_guild(1042769412446494812)  # Replace with your guild ID
                if guild is None:
                    print("Guild not found.")
                    return

                channel = guild.get_channel(1233425018831241306)  # Replace with your channel ID
                if channel is None:
                    print("Channel not found.")
                    return

                bot_member = guild.get_member(bot.user.id)
                if bot_member is None:
                    print("Bot member not found.")
                    return

                permissions = channel.permissions_for(bot_member)
                if permissions.mention_everyone:
                    try:
                        await channel.send(f"@everyone Event '{event_name}' has occurred!")
                    except Exception as e:
                        print(f"Failed to send message: {e}")
                else:
                    try:
                        await channel.send(f"Event '{event_name}' has occurred, but I don't have permission to mention @everyone.")
                    except Exception as e:
                        print(f"Failed to send message: {e}")








"""


"""
PING CMD
"""
@bot.slash_command(description="Replies with pong and latency")
async def ping(interaction: nextcord.Interaction):
    latency = round(bot.latency * 1000)  # Calculate the latency in milliseconds
    await interaction.send(f"Pong! Latency is {latency}ms", ephemeral=False)


"""
BAN CMD
"""
@bot.slash_command(description="Bans a member from the server")
@commands.has_permissions(ban_members=True)
async def ban(interaction: nextcord.Interaction, member: nextcord.Member, reason: str = "No reason provided"):
    if interaction.user.id == allowed_user_id:
        await member.ban(reason=reason)
        await interaction.send(f"{member.display_name} has been banned for {reason}")

    elif "Officer" in [role.name for role in interaction.user.roles]:
        await member.ban(reason=reason)
        await interaction.send(f"{member.display_name} has been banned for {reason}")

    else:
        await interaction.send("You do not have permission to use this command.", ephemeral=False)



"""
BOT EVENTS
"""
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    #check_event_dates.start()

@bot.event
async def on_guild_join(guild):
    print(f"Joined guild: {guild.name} (ID: {guild.id})")

@bot.event
async def on_message(message):
    # Log the message
    with open(log_file, 'a') as file:
        file.write(f"Guild: {message.guild.id} | Channel: {message.channel.id} | User: {message.author.id} | {message.content} | {datetime.now()}\n")
    print(f"Guild: {message.guild.id} | Channel: {message.channel.id} | User: {message.author.id} | {message.content} | {datetime.now()}")

    # Process commands and let the bot respond
    await bot.process_commands(message)



"""
INFO CMD
"""
@bot.slash_command(description="Replies with info about this bot")
async def info(interaction: nextcord.Interaction):
    await interaction.send(f"This is a test bot made by <@1084262700080713768> for VEX Robotics teams. It is currently in development and is not ready for use.", ephemeral=False)


"""
KICK CMD
"""
@bot.slash_command(description="Kicks a member from the server")
@commands.has_permissions(kick_members=True)
async def kick(interaction: nextcord.Interaction, member: nextcord.Member, reason: str = "No reason provided"):
    if interaction.user.id == allowed_user_id:
        await member.kick(reason=reason)
        await interaction.send(f"{member.display_name} has been kicked for {reason}")

    elif "Officer" in [role.name for role in interaction.user.roles]:
        await member.kick(reason=reason)
        await interaction.send(f"{member.display_name} has been kicked for {reason}")

    else:
        await interaction.send("You do not have permission to use this command.", ephemeral=False)


"""
TIPS CMD
"""
@bot.slash_command(description="Replies with a tip about VEX Robotics")
async def tips(interaction: nextcord.Interaction):
    vex_tips = [
      "Check and double-check your robot's measurements before a competition.",
      "Practice driving your robot consistently to improve your skills.",
      "Keep spare parts handy in case of last-minute repairs.",
      "Collaborate with your team members to brainstorm creative solutions.",
      "Stay updated with the latest rule changes and updates from VEX.",
      "Focus on a few key strategies and excel at them rather than trying to do everything.",
      "Use sensors effectively to improve the autonomous capabilities of your robot.",
      "Document your design and build process to learn from your successes and failures.",
      "Stay calm and focused during matches to make quick and effective decisions.",
      "Have fun and enjoy the learning experience of competing in VEX Robotics."
    ]

    random_tip = random.choice(vex_tips)
    await interaction.send(f"{random_tip}", ephemeral=False)


"""
JOKES CMD
"""
@bot.slash_command(description="Replies with a joke about VEX Robotics")
async def jokes(interaction: nextcord.Interaction):
    vex_jokes = [
      "Why did the robot go on a diet? It had too many bytes!",
      "What do you call a robot who likes to take naps? A napster!",
      "How do you stop a robot from charging? You unplug it!",
      "Why was the robot feeling blue? It had a byte taken out of it!",
      "What did the robot say to the vending machine? Can you give me some bytes?",
      "Why did the robot sit on the clock? To be on time!",
      "How does a robot do its hair? With a USB brush!",
      "Why did the robot cross the road? To get to the motherboard!",
      "What do you call a robot that always tells the truth? Trusty Rusty!",
      "Why was the robot cold? It had a byte in its circuits!"
    ]

    random_joke = random.choice(vex_jokes)
    await interaction.send(f"{random_joke}", ephemeral=False)


"""
CODE CMD
"""
@bot.slash_command(description="Provides sample code or programming tips for VEX Robotics robots")
async def code(interaction: nextcord.Interaction):
    code_sample = """

#This is for simple tank drive.

# Library imports
from vex import *

# Begin project code
# Main Controller loop to set motors to controller axis postiions
while True:
    left_motor.set_velocity(controller_1.axis3.position(), PERCENT)
    right_motor.set_velocity(controller_1.axis2.position(), PERCENT)
    left_motor.spin(FORWARD)
    right_motor.spin(FORWARD)
    wait(5, MSEC)
"""

    code_block = f"**Simple Tank Drive** (Python):\n```python\n{code_sample}\n```"
    await interaction.send(code_block, ephemeral=False)


"""
BUILD CMD
"""
@bot.slash_command(description="Provides building tips and techniques for VEX Robotics robots")
async def build(interaction: nextcord.Interaction):
    build_tips = [
        "Use standoffs and spacers to create stable and secure connections between components.",
        "Consider using rubber bands or surgical tubing to add tension or assist in mechanisms like lifts or intakes.",
        "Utilize bearing flats or pillow blocks to support shafts and reduce friction.",
        "Use lock nuts or nylock nuts to prevent screws from loosening due to vibration.",
        "Consider the weight distribution of your robot to ensure stability and prevent tipping.",
        "Use standoff connectors to create multi-level structures and maximize use of space.",
        "Use zip ties to organize and secure wires for a cleaner and more reliable electrical system.",
        "Consider using 3D printed parts to create custom components or brackets for your robot.",
        "Test and iterate on your designs to identify and fix any weaknesses or inefficiencies."
    ]

    random_tip = random.choice(build_tips)
    await interaction.send(f"{random_tip}", ephemeral=False)


"""
PARTS CMD
"""
@bot.slash_command(description="Provides information about specific VEX Robotics parts")
async def parts(interaction: nextcord.Interaction):
    parts_info = [
        {
            "name": "V5 Smart Motor",
            "description": "A high-performance motor used in VEX Robotics competitions. It features built-in encoders for precise control and feedback."
        },
        {
            "name": "V5 Brain",
            "description": "The central control unit for VEX Robotics robots. It features a color touchscreen display and multiple ports for connecting motors, sensors, and controllers."
        },
        {
            "name": "V5 Controller",
            "description": "A handheld controller used to manually control VEX Robotics robots. It features joysticks, buttons, and a color screen for feedback."
        },
        {
            "name": "V5 Robot Battery",
            "description": "A rechargeable battery pack designed for use with VEX Robotics robots. It provides power to the robot's motors and electronics."
        },
        {
            "name": "V5 Vision Sensor",
            "description": "A sensor used to detect and track objects based on their color, size, and shape. It can be used for autonomous navigation and object recognition."
        },
        {
            "name": "V5 Distance Sensor",
            "description": "A sensor used to measure the distance between the sensor and an object. It can be used for obstacle detection and navigation."
        },
        {
            "name": "V5 Inertial Sensor",
            "description": "A sensor used to measure the orientation and movement of a robot. It can be used for balancing, navigation, and motion tracking."
        }
    ]

    # Select a random part info
    part = random.choice(parts_info)
    part_name = part["name"]
    part_description = part["description"]

    # Send the part info as a message
    response = f"**{part_name}**:\n{part_description}"
    await interaction.send(response, ephemeral=False)





"""
EVENT CMDS
"""

@bot.slash_command(description="Creates an event with a name, date, and time")
async def create_event(interaction: nextcord.Interaction, name: str, date: str, time: str):
    try:
        event_date = datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
        with open(events_file, 'a') as file:
            file.write(f"{name},{event_date.strftime('%Y-%m-%d %H:%M')}\n")
        await interaction.send(f"Event '{name}' created for {event_date.strftime('%Y-%m-%d %H:%M')}", ephemeral=False)
    except ValueError:
        await interaction.send("Invalid date or time format. Please use YYYY-MM-DD HH:MM.", ephemeral=False)

@bot.slash_command(description="Shows upcoming events")
async def events(interaction: nextcord.Interaction):
    current_time = datetime.now()
    upcoming_events = []
    with open(events_file, 'r') as file:
        for line in file:
            event_name, event_date_str = line.strip().split(',')
            event_date = datetime.strptime(event_date_str, '%Y-%m-%d %H:%M')
            if event_date > current_time:
                upcoming_events.append(f"{event_name} - {event_date.strftime('%Y-%m-%d %H:%M')}")
    if upcoming_events:
        events_list = "\n".join(upcoming_events)
        await interaction.send(f"Upcoming events:\n{events_list}", ephemeral=False)
    else:
        await interaction.send("No upcoming events.", ephemeral=False)

@bot.slash_command(description="Deletes an event by its name")
async def del_event(interaction: nextcord.Interaction, name: str):
    events = []
    with open(events_file, 'r') as file:
        for line in file:
            event_name, _ = line.strip().split(',')
            if event_name != name:
                events.append(line.strip())
    with open(events_file, 'w') as file:
        file.write("\n".join(events))
    await interaction.send(f"Event '{name}' deleted.", ephemeral=False)




@bot.slash_command(description="Gives you the Events Ping role")
async def events_ping(interaction: nextcord.Interaction):
    guild = interaction.guild
    role_name = "Events Ping"

    # Check if the role already exists
    role = nextcord.utils.get(guild.roles, name=role_name)
    if not role:
        # Create the role if it doesn't exist
        try:
            role = await guild.create_role(name=role_name)
        except nextcord.Forbidden:
            await interaction.send("I do not have permission to create roles.", ephemeral=True)
            return
        except nextcord.HTTPException:
            await interaction.send("Failed to create role. Please try again later.", ephemeral=True)
            return

    # Give the role to the user who invoked the command
    try:
        await interaction.user.add_roles(role)
        await interaction.send("Events Ping role added.", ephemeral=True)
    except nextcord.Forbidden:
        await interaction.send("I do not have permission to add roles.", ephemeral=True)
    except nextcord.HTTPException:
        await interaction.send("Failed to add role. Please try again later.", ephemeral=True)


@bot.slash_command(description="Gives you the Events Tester Ping role")
async def events_ping_tester(interaction: nextcord.Interaction):
    guild = interaction.guild
    role_name = "Events Ping Tester"

    # Check if the role already exists
    role = nextcord.utils.get(guild.roles, name=role_name)
    if not role:
        # Create the role if it doesn't exist
        try:
            role = await guild.create_role(name=role_name)
        except nextcord.Forbidden:
            await interaction.send("I do not have permission to create roles.", ephemeral=True)
            return
        except nextcord.HTTPException:
            await interaction.send("Failed to create role. Please try again later.", ephemeral=True)
            return

    # Give the role to the user who invoked the command
    try:
        await interaction.user.add_roles(role)
        await interaction.send("Events Ping role added.", ephemeral=True)
    except nextcord.Forbidden:
        await interaction.send("I do not have permission to add roles.", ephemeral=True)
    except nextcord.HTTPException:
        await interaction.send("Failed to add role. Please try again later.", ephemeral=True)



"""
Roles
"""




"""
ROLE CMDS
"""
@bot.slash_command(description="Creates a new role with the specified name and color")
async def create_role(interaction: nextcord.Interaction, name: str, color: str):
    if interaction.user.id != allowed_user_id:
        await interaction.send("You do not have permission to use this command.", ephemeral=True)
        return

    # Convert the color string to a discord.Color object
    try:
        color = nextcord.Color(int(color, 16))
    except ValueError:
        await interaction.send("Invalid color format. Please use a hex color code (e.g., #RRGGBB).", ephemeral=True)
        return

    # Create the role with the specified name and color
    try:
        new_role = await interaction.guild.create_role(name=name, color=color)
        await interaction.send(f"Role '{new_role.name}' created with color {color}.", ephemeral=True)
    except nextcord.Forbidden:
        await interaction.send("I do not have permission to create roles.", ephemeral=True)
    except nextcord.HTTPException:
        await interaction.send("Failed to create role. Please try again later.", ephemeral=True)


@bot.slash_command(description="Adds a specified role to a user")
async def role_add(interaction: nextcord.Interaction, member: nextcord.Member, role: nextcord.Role):
    if interaction.user.id != allowed_user_id:
        await interaction.send("You do not have permission to use this command.", ephemeral=True)
        return

    try:
        await member.add_roles(role)
        await interaction.send(f"Role '{role.name}' added to {member.display_name}.", ephemeral=True)
    except nextcord.Forbidden:
        await interaction.send("I do not have permission to add roles.", ephemeral=True)
    except nextcord.HTTPException:
        await interaction.send("Failed to add role. Please try again later.", ephemeral=True)



"""
@bot.slash_command(description="Sets permissions for a specified role")
async def role_perms(interaction: nextcord.Interaction, role: nextcord.Role):
    if interaction.user.id != allowed_user_id:
        await interaction.send("You do not have permission to use this command.", ephemeral=True)
        return

    # Ask for admin permission
    message = await interaction.send("Should the role have admin permissions? (yes/no)", ephemeral=True)
    response = await bot.wait_for("message", check=lambda m: m.author == interaction.user and m.channel == interaction.channel)
    if response.content.lower() not in ["yes", "no"]:
        await interaction.send("Invalid response. Please respond with 'yes' or 'no'.", ephemeral=True)
        return
    admin = response.content.lower() == "yes"

    # Set permissions
    try:
        permissions = nextcord.Permissions(administrator=admin)
        await role.edit(permissions=permissions)
        await interaction.send(f"Permissions updated for role '{role.name}'.", ephemeral=True)
    except nextcord.Forbidden:
        await interaction.send("I do not have permission to edit roles.", ephemeral=True)
    except nextcord.HTTPException:
        await interaction.send("Failed to edit role. Please try again later.", ephemeral=True)

"""




"""
CMDS CMD
"""
"""@bot.slash_command(description="Replies with commands this bot can run")
async def cmds(interaction: nextcord.Interaction):
    await interaction.send("/ping: Replies with pong and latency, \n/ban: Bans a member from the server, \n/info: Replies with info about this bot, \n/cmds: Replies with commands this bot can run, \n/kick: Kicks a member from the server, \n/tips: Kicks a member from the server \n/jokes: Tells a robotics related joke.", ephemeral=False)
"""
bot.run("MTIzNTYwNjY3MjQwODQ0NTA1MQ.G9C1HD.zxYxlbXN5QPFIxPpf6Ls-mFArTi10KwCVnjGnk")
