import { AppSidebar } from "@/components/organisms/app-sidebar"
import {
    SidebarInset,
    SidebarProvider,
    SidebarTrigger,
} from "@/components/atoms/sidebar"
import { ReactNode } from "react"
import { NavUser } from "../molecules/nav-user"
import { SearchBar } from "../molecules/search-bar"

export function LayoutHome({ children }: { children: ReactNode }) {
    return (
        <SidebarProvider className="w-full">
            <AppSidebar />
            <SidebarInset className="bg-salmon-50 flex flex-col relative">
                <header className="flex h-12 shrink-0 bg-zinc-50 py-10 items-center sticky top-0 z-10 transition-[width,height] ease-linear group-has-[[data-collapsible=icon]]/sidebar-wrapper:h-12 w-full border border-b-salmon-300">
                    <div className="flex items-center gap-2 px-4 justify-center flex-1">
                        <SidebarTrigger />
                        <SearchBar />
                        <NavUser />
                    </div>
                </header>
                <div className="flex flex-1 flex-col gap-4 p-4">{children}</div>
            </SidebarInset>
        </SidebarProvider>
    )
}
