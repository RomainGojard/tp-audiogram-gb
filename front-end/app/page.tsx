"use client"

import { useState } from "react"
import { runDefaultPipeline, trainModel, getPrediction } from "@/lib/api";
import PredictionForm from "@/components/prediction-form"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Loader2 } from "lucide-react"
import { ThemeToggle } from "@/components/theme-toggle"

export default function Home() {
  const [loading, setLoading] = useState<string | null>(null)
  const [result, setResult] = useState<any>(null)
  const [error, setError] = useState<string | null>(null)

  const handleRunPipeline = async (type: "default" | "train") => {
    setLoading(type === "default" ? "default" : "train")
    setResult(null)
    setError(null)

    try {
      const response = type === "default" ? await runDefaultPipeline() : await trainModel()

      setResult(response)
    } catch (err: any) {
      setError(err.message || "An error occurred")
    } finally {
      setLoading(null)
    }
  }

  const handlePrediction = async (data: any) => {
    setLoading("predict")
    setResult(null)
    setError(null)

    try {
      const prediction = await getPrediction(data)
      setResult(prediction)
    } catch (err: any) {
      setError(err.message || "An error occurred")
    } finally {
      setLoading(null)
    }
  }

  return (
    <main className="container mx-auto p-4 max-w-4xl">
      <header className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">Tonal Exam Predictor</h1>
        <ThemeToggle />
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        <Card>
          <CardHeader>
            <CardTitle>Pipeline Execution</CardTitle>
            <CardDescription>Run data processing pipelines</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="flex flex-col gap-3">
              <Button onClick={() => handleRunPipeline("default")} disabled={loading !== null} className="w-full">
                {loading === "default" && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
                Run Full Pipeline
              </Button>

              <Button onClick={() => handleRunPipeline("train")} disabled={loading !== null} className="w-full">
                {loading === "train" && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
                Train Model
              </Button>
            </div>
          </CardContent>
        </Card>

        <PredictionForm onSubmit={handlePrediction} isLoading={loading === "predict"} />
      </div>

      {error && (
        <Card className="mb-6 border-red-300 bg-red-50">
          <CardContent className="pt-6">
            <p className="text-red-600">{error}</p>
          </CardContent>
        </Card>
      )}

      {result && (
        <Card>
          <CardHeader>
            <CardTitle>Result</CardTitle>
          </CardHeader>
          <CardContent>
            <pre className="bg-gray-100 p-4 rounded-md overflow-auto max-h-96">{JSON.stringify(result, null, 2)}</pre>
          </CardContent>
        </Card>
      )}
    </main>
  )
}
