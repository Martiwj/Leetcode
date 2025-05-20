

fun sumOfEven(list: List<Int>): Int = list.filter {it % 2 == 0}.sum()


fun main() {
    val list = listOf(1, 2, 3, 4, 5, 6)
    println(sumOfEven(list))
}
