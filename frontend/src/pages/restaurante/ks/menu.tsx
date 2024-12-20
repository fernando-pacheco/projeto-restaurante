import { Logo } from "@/components/atoms/logo"
import { LayoutHome } from "@/components/templates/layout-home"

export function KsMenu() {
    return (
        <LayoutHome>
            <div className="flex gap-4 items-center">
                <Logo
                    alt="team-logo"
                    src="/static/ks-logo.png"
                    width={120}
                    className="rounded-full bg-white p-2"
                />
                <span className="font-semibold text text-4xl">KS BURGUER</span>
            </div>
        </LayoutHome>
    )
}
