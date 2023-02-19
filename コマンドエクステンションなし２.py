import discord
from discord import(
    app_commands,
    ui,
    ButtonStyle
)


from discord.app_commands import CommandTree

TOKEN = "API TOKEN"

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
#鯖設定　guild = discord.guild(id=)

@client.event
async def on_ready():
    print("起動完了")
    await tree.sync()

@tree.command(name="promotion",description="アクティブクリエイターが宣伝するためのコマンドです。")
@app_commands.describe(role="誰に送るかを指定。",text="送りたい文章を書き込んでください。")
async def promotion_command(interaction: discord.Interaction,role:discord.Role,text:str):
    embed = discord.Embed(title="新作の宣伝です！", description=text)
    embed.set_author(
        #メッセージの部分をコマンド使用者に変える(あっているのか確認！)
       name=interaction.user.display_name, 
       #同じくコメント使用者に変える（出来ているのか確認！）
       icon_url=interaction.user.display_avatar.url, 
   ).set_footer(
       text=f"transfar from {interaction.user.display_name}",
       icon_url=interaction.user.display_avatar.url,
   )
    await interaction.response.send_message(f"{role}", embed=embed, ephemeral=True)

    #channnelはコマンドで指定できない　UI参照　UIでOKが出たらroleのところも含めて引数にして他のところにawait massageで送信する


    #await delete_original_response()


    '''わかるようになったらUIを追加すること
    url_view = ui.View()
    url_view.add_item(
        ui.Button(
            label="Go to Message", style=ButtonStyle.url, url=message.jump_url
        )
    )
    await interaction.response.send_message(f"{role}", embed=embed, view=url_view)'''
   

client.run(TOKEN)



'''UIを実装するほかない
まず前の人のを参考にゼロから作り直してみるのがいいかもしれない
試作２
'''
#   raise CommandInvokeError(self, e) from e
#discord.app_commands.errors.CommandInvokeError: Command 'promotion' raised an exception: AttributeError: 'Interaction' object has no attribute 'massage'
