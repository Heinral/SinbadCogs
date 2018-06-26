from redbot.core import commands


class RoleSyntaxConverter(commands.RoleConverter):
    async def convert(self, ctx: commands.Context, argument: str):
        args = [c.strip() for c in argument.split(",")]
        ret = {"+": set(), "-": set()}

        for arg in args:
            ret[arg[0]].update(await super().convert(ctx, arg[1:]))

        if not (ret["+"] or ret["-"]):
            raise commands.BadArgument("This requires at least one role operation.")

        if not ret["+"].isdisjoint(ret["-"]):
            raise commands.BadArgument("I really can't add and remove the same role.")
        return ret


class ComplexRoleSyntaxConverter(RoleSyntaxConverter):
    async def convert(self, ctx: commands.Context, argument: str):
        args = [c.strip() for c in argument.split(";")]
        if len(args) != 2:
            raise commands.BadArgument("Requires both a search and operation")

        ret = ((await super().convert(arg)) for arg in args)