import { SidebarMenu, SidebarMenuItem } from "@/components/atoms/sidebar"
import { ElementType } from "react"

interface TeamLogoProps {
    team: { logo: ElementType }
}

export function TeamLogo({ team }: TeamLogoProps) {
    return (
        <SidebarMenu>
            <SidebarMenuItem className="flex justify-center py-8">
                <div className="flex items-center justify-center text-salmon-600">
                    <team.logo className="size-8" />
                </div>
            </SidebarMenuItem>
        </SidebarMenu>
    )
}
