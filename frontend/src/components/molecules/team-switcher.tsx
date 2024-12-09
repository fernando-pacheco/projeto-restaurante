"use client"

import {
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    useSidebar,
} from "@/components/atoms/sidebar"
import { useState } from "react"

export function TeamSwitcher({
    teams,
}: {
    teams: {
        name: string
        logo: React.ElementType
        plan: string
    }[]
}) {
    const { isMobile } = useSidebar()
    const [activeTeam, setActiveTeam] = useState(teams[0])

    return (
        <SidebarMenu>
            <SidebarMenuItem>
                <SidebarMenuButton
                    size="lg"
                    className="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground flex justify-center"
                >
                    <div className="aspect-square size-8 rounded-lg bg-salmon-100 flex items-center justify-center text-salmon-600 border border-salmon-900">
                        <activeTeam.logo className="size-4" />
                    </div>
                </SidebarMenuButton>
            </SidebarMenuItem>
        </SidebarMenu>
    )
}
