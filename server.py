from fastmcp import FastMCP

mcp = FastMCP("myMCP")

@mcp.tool()
def add(a: int, b: int):
    return a + b


if __name__ == "__main__":
    mcp.run(transport="http")