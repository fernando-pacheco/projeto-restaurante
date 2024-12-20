import { Toaster } from "sonner"
import { X } from "lucide-react"
import { AppRoutes } from "./routes/routes"

export function App() {
    return (
        <div>
            <Toaster
                icons={{
                    error: (
                        <X className="rounded-full bg-[#ed3615] size-4 text-salmon-50 p-0.5" />
                    ),
                }}
            />
            <AppRoutes />
        </div>
    )
}
