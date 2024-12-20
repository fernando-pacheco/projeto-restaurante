import { SidebarMenu, SidebarMenuItem } from "@/components/atoms/sidebar"
import { Logo } from "../atoms/logo"

interface TeamLogoProps {
    team: { logo: string }
}

export function TeamLogo({ team }: TeamLogoProps) {
    return (
        <SidebarMenu>
            <SidebarMenuItem className="flex justify-center">
                <div className="flex items-center justify-center">
                    <Logo alt="team-logo" src={team.logo} width={200} />
                </div>
            </SidebarMenuItem>
        </SidebarMenu>
    )
}
