import { useState } from "react"
import { Mic, X } from "lucide-react"
import { motion } from "framer-motion"
import "./AureaWidget.css"

const AureaWidget = () => {
  const [open, setOpen] = useState(false)

  return (
    <div className="aurea-container">
      {open ? (
        <motion.div
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          className="aurea-widget"
        >
          <div className="aurea-header">
            <h2 className="aurea-title">✨ Aurea</h2>
            <button onClick={() => setOpen(false)} className="aurea-close">
              <X className="icon" />
            </button>
          </div>
          <div className="aurea-body">
            Listening for your commands…
          </div>
          <button className="aurea-speak-btn">
            <Mic className="icon" /> Speak
          </button>
        </motion.div>
      ) : (
        <button
          onClick={() => setOpen(true)}
          className="aurea-mic-btn"
        >
          <Mic className="icon" />
        </button>
      )}
    </div>
  )
}

export default AureaWidget
