import { BadgeCheck, Bell, CreditCard, LogOut, Sparkles } from "lucide-react"

import { Avatar, AvatarFallback, AvatarImage } from "@/components/atoms/avatar"
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuTrigger,
} from "@/components/atoms/dropdown-menu"
import {
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    useSidebar,
} from "@/components/atoms/sidebar"
import { useUser } from "@/hooks/use-user"
import { revokeToken } from "@/utils/token"
import { useNavigate } from "react-router-dom"
import { setupToast } from "@/utils/setup-toast"

export function NavUser() {
    const { isMobile } = useSidebar()
    const { userData } = useUser()
    const navigate = useNavigate()

    function handleLogout() {
        revokeToken()
        setupToast({
            id: "logout",
            description: "Espero te ver novamente logo.",
            status: "success",
            title: "Você saiu da sua conta :(",
        })
        navigate("/")
    }

    return (
        <SidebarMenu className="w-auto">
            <SidebarMenuItem>
                <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                        <SidebarMenuButton
                            size="lg"
                            className="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground flex justify-end py-7 px-4 bg-salmon-600 hover:bg-salmon-500 text-salmon-50 gap-5 hover:text-salmon-50 drop-shadow-md"
                        >
                            <div className="grid text-right text-sm leading-tight">
                                <span className="truncate font-semibold">
                                    {`${userData.name} ${userData.surname || "."}`}
                                </span>
                                <span className="truncate text-xs">
                                    {userData.email}
                                </span>
                            </div>
                            <Avatar className="h-10 w-10 rounded-lg">
                                <AvatarImage
                                    src={userData.avatar}
                                    alt={userData.name}
                                />
                                <AvatarFallback className="rounded-lg bg-salmon-200 text-salmon-950">
                                    {userData.name[0]}
                                    {userData.surname[0] || "."}
                                </AvatarFallback>
                            </Avatar>
                        </SidebarMenuButton>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent
                        className="w-[--radix-dropdown-menu-trigger-width] min-w-56 rounded-lg"
                        side={isMobile ? "bottom" : "right"}
                        align="end"
                        sideOffset={4}
                    >
                        <DropdownMenuLabel className="p-0 font-normal">
                            <div className="flex items-center gap-2 px-1 py-1.5 text-left text-sm">
                                <Avatar className="h-10 w-10 rounded-lg">
                                    <AvatarImage
                                        src={userData.avatar}
                                        alt={userData.name}
                                    />
                                    <AvatarFallback className="rounded-lg bg-salmon-200">
                                        {userData.name[0]}
                                        {userData.surname[0] || "."}
                                    </AvatarFallback>
                                </Avatar>
                                <div className="grid flex-1 text-left text-sm leading-tight">
                                    <span className="truncate font-semibold">
                                        {userData.username}
                                    </span>
                                    <span className="truncate text-xs">
                                        {userData.email}
                                    </span>
                                </div>
                            </div>
                        </DropdownMenuLabel>

                        <DropdownMenuSeparator />
                        <DropdownMenuGroup>
                            <DropdownMenuItem>
                                <Sparkles />
                                Upgrade to Pro
                            </DropdownMenuItem>
                        </DropdownMenuGroup>
                        <DropdownMenuSeparator />
                        <DropdownMenuGroup>
                            <DropdownMenuItem>
                                <BadgeCheck />
                                Account
                            </DropdownMenuItem>
                            <DropdownMenuItem>
                                <CreditCard />
                                Billing
                            </DropdownMenuItem>
                            <DropdownMenuItem>
                                <Bell />
                                Notifications
                            </DropdownMenuItem>
                        </DropdownMenuGroup>
                        <DropdownMenuSeparator />
                        <DropdownMenuItem>
                            <button
                                className="flex gap-2 w-full"
                                onClick={() => handleLogout()}
                            >
                                <LogOut />
                                Sair
                            </button>
                        </DropdownMenuItem>
                    </DropdownMenuContent>
                </DropdownMenu>
            </SidebarMenuItem>
        </SidebarMenu>
    )
}
