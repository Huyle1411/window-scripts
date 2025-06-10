private fun readStr() = readln()
private fun readInt() = readStr().toInt()
private fun readLong() = readStr().toLong()
private fun readDouble() = readStr().toDouble()
private fun readStrings() = readStr().split(" ")
private fun readInts() = readStrings().map { it.toInt() }
private fun readLongs() = readStrings().map { it.toLong() }
private fun readDoubles() = readStrings().map { it.toDouble() }

private fun gcd(a: Long, b: Long): Long = if (b == 0) a else gcd(b, a % b)
private fun lcm(a: Long, b: Long): Long = a / gcd(a, b) * b
private fun pow(base: Long, exp: Long, mod: Long = 1_000_000_007): Long {
    var result = 1L
    var b = base % mod
    var e = exp
    while (e > 0) {
        if (e % 2 == 1L) result = (result * b) % mod
        b = (b * b) % mod
        e /= 2
    }
    return result
}

private val output = StringBuilder()

fun main() {
    var t = 1
    t = readInt()
    repeat(t) {
        solve()
    }
    print(output)
}

fun solve() {
    output.append("\n")
}
