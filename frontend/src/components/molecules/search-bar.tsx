import { Search } from "lucide-react"
import { Input } from "../atoms/input"
import { Button } from "../atoms/button"
import { FormEvent } from "react"

export function SearchBar() {
    function handleSubmit(e: FormEvent<HTMLFormElement>) {
        e.preventDefault()
        const formData = new FormData(e.currentTarget)
        console.log(formData.get("search"))
    }

    return (
        <form
            onSubmit={handleSubmit}
            className="flex flex-1 justify-center items-center"
        >
            <Button variant={"search"} type="submit">
                <Search />
            </Button>
            <Input
                id="search-bar"
                name="search"
                type="text"
                placeholder="Pesquisar"
                className="bg-transparent w-[400px] rounded-none rounded-r-lg focus-visible:ring-0 focus-visible:ring-offset-0"
            />
        </form>
    )
}
