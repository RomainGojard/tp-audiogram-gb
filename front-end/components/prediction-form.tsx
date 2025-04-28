"use client"

import type React from "react"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Loader2 } from "lucide-react"

interface PredictionFormProps {
  onSubmit: (data: any) => void
  isLoading: boolean
}

export default function PredictionForm({ onSubmit, isLoading }: PredictionFormProps) {
  const [formData, setFormData] = useState({
    before_exam_125_Hz: "",
    before_exam_250_Hz: "",
    before_exam_500_Hz: "",
    before_exam_1000_Hz: "",
    before_exam_2000_Hz: "",
    before_exam_4000_Hz: "",
    before_exam_8000_Hz: "",
  })

  const [errors, setErrors] = useState<Record<string, boolean>>({})

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target

    // Vérifiez si la valeur est un nombre valide
    const isValid = value === "" || !isNaN(Number(value))

    // Mettez à jour les erreurs
    setErrors((prev) => ({ ...prev, [name]: !isValid }))

    // Mettez à jour les données du formulaire
    setFormData((prev) => ({ ...prev, [name]: value }))
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()

    // Convert string values to numbers where appropriate
    const processedData = Object.entries(formData).reduce(
      (acc, [key, value]) => {
        acc[key] = value === "" ? "" : isNaN(Number(value)) ? value : Number(value)
        return acc
      },
      {} as Record<string, string | number>,
    )

    onSubmit(processedData)
  }

  // Vérifiez si le bouton doit être désactivé
  const isSubmitDisabled =
    Object.values(formData).some((value) => value === "") || // Vérifie si un champ est vide
    Object.values(errors).some((error) => error) // Vérifie s'il y a des erreurs

  return (
    <Card>
      <CardHeader>
        <CardTitle>Prediction</CardTitle>
        <CardDescription>Enter patient data to predict prosthetic gain</CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="grid grid-cols-1 gap-4">
            {Object.keys(formData).map((key) => (
              <div key={key} className="space-y-2">
                <Label htmlFor={key}>{key.replace(/_/g, " ")}</Label>
                <Input
                  id={key}
                  name={key}
                  value={formData[key as keyof typeof formData]}
                  onChange={handleChange}
                  placeholder="Enter value"
                  className={errors[key] ? "border-red-500 focus:ring-red-500" : ""}
                />
                {errors[key] && <p className="text-red-500 text-sm">Please enter a valid number</p>}
              </div>
            ))}
          </div>

          <Button type="submit" disabled={isLoading || isSubmitDisabled} className="w-full">
            {isLoading && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
            Get Prediction
          </Button>
        </form>
      </CardContent>
    </Card>
  )
}
