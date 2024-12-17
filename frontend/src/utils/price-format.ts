export function priceFormat(number: number) {
    const priceformated = number.toLocaleString("pt-BR", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
    })

    return `R$ ${priceformated}`
}
