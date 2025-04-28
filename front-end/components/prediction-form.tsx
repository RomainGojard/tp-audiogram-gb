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

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target
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

  return (
    <Card>
      <CardHeader>
        <CardTitle>Prediction</CardTitle>
        <CardDescription>Enter patient data to predict prosthetic gain</CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="grid grid-cols-1 gap-4">
            <div className="space-y-2">
              <Label htmlFor="before_exam_125_Hz">Before Exam 125 Hz</Label>
              <Input
                id="before_exam_125_Hz"
                name="before_exam_125_Hz"
                value={formData.before_exam_125_Hz}
                onChange={handleChange}
                placeholder="Enter value"
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="before_exam_250_Hz">Before Exam 250 Hz</Label>
              <Input
                id="before_exam_250_Hz"
                name="before_exam_250_Hz"
                value={formData.before_exam_250_Hz}
                onChange={handleChange}
                placeholder="Enter value"
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="before_exam_500_Hz">Before Exam 500 Hz</Label>
              <Input
                id="before_exam_500_Hz"
                name="before_exam_500_Hz"
                value={formData.before_exam_500_Hz}
                onChange={handleChange}
                placeholder="Enter value"
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="before_exam_1000_Hz">Before Exam 1000 Hz</Label>
              <Input
                id="before_exam_1000_Hz"
                name="before_exam_1000_Hz"
                value={formData.before_exam_1000_Hz}
                onChange={handleChange}
                placeholder="Enter value"
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="before_exam_2000_Hz">Before Exam 2000 Hz</Label>
              <Input
                id="before_exam_2000_Hz"
                name="before_exam_2000_Hz"
                value={formData.before_exam_2000_Hz}
                onChange={handleChange}
                placeholder="Enter value"
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="before_exam_4000_Hz">Before Exam 4000 Hz</Label>
              <Input
                id="before_exam_4000_Hz"
                name="before_exam_4000_Hz"
                value={formData.before_exam_4000_Hz}
                onChange={handleChange}
                placeholder="Enter value"
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="before_exam_8000_Hz">Before Exam 8000 Hz</Label>
              <Input
                id="before_exam_8000_Hz"
                name="before_exam_8000_Hz"
                value={formData.before_exam_8000_Hz}
                onChange={handleChange}
                placeholder="Enter value"
              />
            </div>
          </div>

          <Button type="submit" disabled={isLoading} className="w-full">
            {isLoading && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
            Get Prediction
          </Button>
        </form>
      </CardContent>
    </Card>
  )
}
