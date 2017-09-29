import asyncio


class GameManager:
    # Manage ongoing games of a type, including storage, add and removal
    def __init__(self, bot):
        self.bot = bot
        self.games_in_progress = {}

    def is_valid_new_game(self, host):
        return host not in self.games_in_progress

    async def invalid_game_error(self):
        await self.bot.say("Please finish your current game first.")

    def add_game(self, game):
        self.games_in_progress[game.host] = game

    def get_game(self, ctx):
        author = ctx.message.author
        if author in self.games_in_progress:
            return self.games_in_progress[author]

    def remove_game(self, ctx):
        author = ctx.message.author
        self.games_in_progress.pop(author)

    async def set_time_limit(self, game):
        host = game.host_name
        await asyncio.sleep(100.0)
        await self.bot.say(f"{host} has 20 seconds left!")
        await asyncio.sleep(20.0)
        await self.bot.say(f"Time limit elapsed. {host}'s game has ended.")
        self.games_in_progress.pop(game.host)
        return True
